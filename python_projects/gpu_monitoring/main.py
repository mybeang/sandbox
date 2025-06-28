import time
import gpu_state
import json
from database import InfluxDbSdk


def main():
    while True:
        metric_data = gpu_state.get()
        print(json.dumps(metric_data, indent=2))
        InfluxDbSdk.write(metric_data)
        time.sleep(1)


if __name__ == "__main__":
    main()
