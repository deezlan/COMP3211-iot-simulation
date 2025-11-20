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

def run_test(name):
    print(f"\n{name}: Starting test")
    avg_durations = []

    for size in test_sizes:
        print(f"Running {size} sequential requests")
        durations = []

        for _ in range(size):
            start = time.perf_counter()
            try:
                r = requests.get(URL)
                r.raise_for_status()
            except:
                pass
            end = time.perf_counter()
            durations.append(round((end - start) * 1000, 2))  # in ms

        avg = sum(durations) / len(durations)
        print(f"Average for {size}: {avg:.2f} ms")
        avg_durations.append(avg)

    return avg_durations

# Run tests
cold_results = run_test("Cold Start")
warm_results = run_test("Warm Start")

# Plot and save the results
plt.figure(figsize=(10, 6))
plt.plot(test_sizes, cold_results, marker='o', label="Cold Start", color='blue')
plt.plot(test_sizes, warm_results, marker='o', label="Warm Start", color='red')
plt.title("Task 2: GetSensorStats – Cold vs Warm Start Performance")
plt.xlabel("Number of Sequential Requests")
plt.ylabel("Average Response Time (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task2_cold_vs_warm_comparison.png")
plt.show()
