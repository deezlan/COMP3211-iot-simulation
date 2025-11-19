import requests
import time
import matplotlib.pyplot as plt
import os

URL = os.environ["FUNC_URL_GENERATE_SENSOR_DATA"]

# Warm up to avoid cold start impact
## Not needed anymore as cold starts are part of the test
# print("Warming up function...")
# for _ in range(50):
#     try:
#         requests.get(URL)
#     except:
#         pass
# time.sleep(2)

# Real tests
test_sizes = [10, 20, 50, 100]
# test_sizes = [100, 50, 20, 10] # Reversed to diagnose cold start issues
results = []

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
plt.plot(test_sizes, cold_results, marker='o', label="Cold Start")
plt.plot(test_sizes, warm_results, marker='o', label="Warm Start")
plt.title("Task 1: Azure Function Performance – Cold vs Warm Start")
plt.xlabel("Number of Sequential Requests")
plt.ylabel("Average Response Time (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("task1_cold_vs_warm_comparison.png")
plt.show()
