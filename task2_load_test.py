import requests
import time
import matplotlib.pyplot as plt
import json
import os

with open("local.settings.json") as f:
    settings = json.load(f)
    for k, v in settings.get("Values", {}).items():
        os.environ[k] = v

URL = os.environ["FUNC_URL_GET_SENSOR_STATS"]

test_sizes = [10, 20, 50, 100]

def run_test():
    avg_durations = []

    for size in test_sizes:
        print(f"\nRunning {size} requests")
        durations = []

        for _ in range(size):
            start = time.perf_counter()
            try:
                response = requests.get(URL)
                response.raise_for_status()
            except:
                pass
            end = time.perf_counter()
            durations.append(round((end - start) * 1000, 2))  # in ms

        avg = sum(durations) / len(durations)
        print(f"Average for {size} requests: {avg:.2f} ms")
        avg_durations.append(avg)

    return avg_durations

def plot_results(results):
    plt.figure(figsize=(10, 6))
    plt.plot(test_sizes, results, marker='o', color='green')
    plt.title("Task 2: GetSensorStats Function Performance")
    plt.xlabel("Number of Sequential Requests")
    plt.ylabel("Average Response Time (ms)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("task2_scalability_graph.png")
    plt.show()

if __name__ == "__main__":
    results = run_test()
    plot_results(results)
