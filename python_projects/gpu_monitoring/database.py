import os
from influxdb_client_3 import (
  InfluxDBClient3, InfluxDBError, Point, WritePrecision,
  WriteOptions, write_client_options)


def success(self, data: str):
    print(f"Successfully wrote batch: data: {data}")


def error(self, data: str, exception: InfluxDBError):
    print(f"Failed writing batch: config: {self}, data: {data} due: {exception}")


def retry(self, data: str, exception: InfluxDBError):
    print(f"Failed retry writing batch: config: {self}, data: {data} retry: {exception}")


class InfluxDbSdk(object):
    HOST = "http://localhost"
    TOKEN = os.getenv("INFLUXDB3_AUTH_TOKEN")
    DB = "gpu_metrics"

    @classmethod
    def reform(cls, ts, data):
        return (Point(cls.DB)
                .tag("gpu_name", data['name'])
                .field("gpu_util", data['utilization']['gpu'])
                .field("mem_used_mb", data['memory']['used'])
                .field("mem_total_mb", data['memory']['total'])
                .field("temp_celsius", data['utilization']['temp'])
                .time(ts, WritePrecision.NS))

    @classmethod
    def write(cls, bulk_data):
        write_options = WriteOptions(batch_size=500,
                                     flush_interval=10_000,
                                     jitter_interval=2_000,
                                     retry_interval=5_000,
                                     max_retries=5,
                                     max_retry_delay=30_000,
                                     exponential_base=2)
        wco = write_client_options(success_callback=success,
                                   error_callback=error,
                                   retry_callback=retry,
                                   write_options=write_options)

        points = []
        for data in bulk_data:
            for metric in data['metrics']:
                points.append(cls.reform(data['timestamp'], metric))

        with InfluxDBClient3(host=cls.HOST,
                             write_port_overwrite=8181,
                             query_port_overwrite=8181,
                             token=cls.TOKEN,
                             database=cls.DB,
                             verify_ssl=False,
                             write_client_options=wco) as client:
            client.write(points, write_precision='s')
