import ctypes
import time

# 먼저 nvml.dll 명시적으로 로딩
nvml_path = r"C:\Windows\System32\nvml.dll"
nvmlLib = ctypes.CDLL(nvml_path)
# path 추가로 하니 계속 잘못된 path 를 이용해서 읽고 있어 위 코드가 추가됬음.

# 그런 다음 pynvml import
import pynvml

def get():
    pynvml.nvmlLib = nvmlLib  # 핵심: 강제로 nvmlLib 대체
    pynvml.NVML_SUCCESS = 0   # 이 줄이 없으면 nvmlInit 에서 실패 가능

    # 정상 로딩 확인 및 사용
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()
    metrics = []
    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        name = pynvml.nvmlDeviceGetName(handle)
        mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)

        metrics.append({
            "name": name.decode('utf-8'),
            "memory": {
                "used": mem.used / 1024 ** 2,
                "total": mem.total / 1024 ** 2,
            },
            "utilization": {
                "gpu": util.gpu,
                "temp": temp
            }
        })
    return {"timestamp": time.time_ns(), "metrics": metrics}
