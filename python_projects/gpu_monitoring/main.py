import time
import gpu_state
import json
from database import InfluxDbSdk
import threading
import queue


def collector_task(m_queue):
    while True:
        m_queue.put(gpu_state.get())
        time.sleep(1)

def write_task(m_queue):
    while True:
        metric_bulk_data = []
        while not m_queue.empty():
            try:
                metric_bulk_data.append(m_queue.get_nowait())
            except m_queue.Empty:
                break
        print(json.dumps(metric_bulk_data, indent=2))
        InfluxDbSdk.write(metric_bulk_data)
        time.sleep(2)


def main():
    m_queue = queue.Queue()
    th_collector = threading.Thread(target=collector_task, args=(m_queue,))
    th_write = threading.Thread(target=write_task, args=(m_queue,))

    th_collector.start()
    th_write.start()

    th_collector.join()
    th_write.join()


if __name__ == "__main__":
    main()
