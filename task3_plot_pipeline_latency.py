import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

# Timestamps in azure_task3_logs.csv collected from Azure Monitor logs
timestamps = [
    # [T1] when Task 3a timer triggers, [T2] when Task 1 HTTP function responds, [T3] when SQL trigger fires, [T4] measured when Task 2 HTTP function responds
    ("2025-11-21T16:07:30.000272+00:00", "2025-11-21T16:07:30.098898+00:00", "2025-11-21T16:07:30.912178+00:00", "2025-11-21T16:07:31.010238+00:00"),
    ("2025-11-21T16:07:20.003118+00:00", "2025-11-21T16:07:20.090806+00:00", "2025-11-21T16:07:20.619372+00:00", "2025-11-21T16:07:20.717268+00:00"),
    ("2025-11-21T16:07:10.004719+00:00", "2025-11-21T16:07:10.106437+00:00", "2025-11-21T16:07:10.326115+00:00", "2025-11-21T16:07:10.447037+00:00"),
    ("2025-11-21T16:07:00.000838+00:00", "2025-11-21T16:07:00.115600+00:00", "2025-11-21T16:07:01.046922+00:00", "2025-11-21T16:07:01.142774+00:00"),
    ("2025-11-21T16:06:50.000832+00:00", "2025-11-21T16:06:50.122744+00:00", "2025-11-21T16:06:50.768794+00:00", "2025-11-21T16:06:50.857637+00:00"),
    ("2025-11-21T16:06:40.004978+00:00", "2025-11-21T16:06:40.116145+00:00", "2025-11-21T16:06:40.510389+00:00", "2025-11-21T16:06:40.600673+00:00"),
    ("2025-11-21T16:06:30.001519+00:00", "2025-11-21T16:06:30.110293+00:00", "2025-11-21T16:06:30.248241+00:00", "2025-11-21T16:06:30.333662+00:00"),
    ("2025-11-21T16:06:20.000878+00:00", "2025-11-21T16:06:20.103113+00:00", "2025-11-21T16:06:20.945718+00:00", "2025-11-21T16:06:21.071296+00:00"),
    ("2025-11-21T16:06:10.004159+00:00", "2025-11-21T16:06:10.109511+00:00", "2025-11-21T16:06:10.674624+00:00", "2025-11-21T16:06:10.768592+00:00"),
    ("2025-11-21T16:06:00.004863+00:00", "2025-11-21T16:06:00.103503+00:00", "2025-11-21T16:06:00.409231+00:00", "2025-11-21T16:06:00.506187+00:00"),
    ("2025-11-21T16:05:50.002678+00:00", "2025-11-21T16:05:50.123856+00:00", "2025-11-21T16:05:51.154298+00:00", "2025-11-21T16:05:51.235195+00:00"),
    ("2025-11-21T16:05:40.003137+00:00", "2025-11-21T16:05:40.117705+00:00", "2025-11-21T16:05:40.899494+00:00", "2025-11-21T16:05:40.984291+00:00"),
    ("2025-11-21T16:05:30.001823+00:00", "2025-11-21T16:05:30.743064+00:00", "2025-11-21T16:05:31.631602+00:00", "2025-11-21T16:05:31.724933+00:00"),
    ("2025-11-21T16:05:20.001680+00:00", "2025-11-21T16:05:20.129585+00:00", "2025-11-21T16:05:20.366263+00:00", "2025-11-21T16:05:20.445454+00:00"),
    ("2025-11-21T16:05:10.000654+00:00", "2025-11-21T16:05:10.121609+00:00", "2025-11-21T16:05:11.113520+00:00", "2025-11-21T16:05:11.199670+00:00"),
    ("2025-11-21T16:05:00.007781+00:00", "2025-11-21T16:05:00.146271+00:00", "2025-11-21T16:05:00.854971+00:00", "2025-11-21T16:05:00.932823+00:00"),
    ("2025-11-21T16:04:50.001718+00:00", "2025-11-21T16:04:50.124170+00:00", "2025-11-21T16:04:50.570976+00:00", "2025-11-21T16:04:50.666321+00:00"),
    ("2025-11-21T16:04:40.004448+00:00", "2025-11-21T16:04:40.805316+00:00", "2025-11-21T16:04:41.301400+00:00", "2025-11-21T16:04:41.397661+00:00"),
    ("2025-11-21T16:04:30.001583+00:00", "2025-11-21T16:04:30.119015+00:00", "2025-11-21T16:04:31.002309+00:00", "2025-11-21T16:04:31.107009+00:00"),
    ("2025-11-21T16:04:20.004583+00:00", "2025-11-21T16:04:20.125822+00:00", "2025-11-21T16:04:20.728125+00:00", "2025-11-21T16:04:20.823266+00:00"),
]

# Compute durations
t1_to_t2, t2_to_t3, t3_to_t4, t1_to_t4 = [], [], [], []
for t1, t2, t3, t4 in timestamps:
    dt1, dt2, dt3, dt4 = map(datetime.fromisoformat, (t1, t2, t3, t4))
    t1_to_t2.append((dt2 - dt1).total_seconds())
    t2_to_t3.append((dt3 - dt2).total_seconds())
    t3_to_t4.append((dt4 - dt3).total_seconds())
    t1_to_t4.append((dt4 - dt1).total_seconds())

# Plot
cycles = list(range(1, len(timestamps)+1))
plt.figure(figsize=(12, 6))
plt.plot(cycles, t1_to_t4, label="Total Pipeline (T4 - T1)", marker='o')
plt.plot(cycles, t1_to_t2, label="Task 1 HTTP (T2 - T1)", marker='o')
plt.plot(cycles, t2_to_t3, label="SQL Trigger Delay (T3 - T2)", marker='o')
plt.plot(cycles, t3_to_t4, label="Task 2 HTTP (T4 - T3)", marker='o')
plt.title("Task 3: End-to-End Pipeline Timing per Cycle")
plt.xlabel("Cycle Number")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("task3_pipeline_latency_graph.png")
plt.show()

# Plotting as stacked bar chart
x = np.arange(len(timestamps))
bar_width = 0.6

plt.figure(figsize=(14, 6))
plt.bar(x, t1_to_t2, width=bar_width, label="Task 1 HTTP (T2 - T1)", color="skyblue")
plt.bar(x, t2_to_t3, width=bar_width, bottom=t1_to_t2, label="SQL Trigger Delay (T3 - T2)", color="lightgreen")
plt.bar(x, t3_to_t4, width=bar_width, bottom=np.array(t1_to_t2)+np.array(t2_to_t3), label="Task 2 HTTP (T4 - T3)", color="salmon")

plt.plot(x, t1_to_t4, label="Total Pipeline Time (T4 - T1)", color="black", marker="o", linewidth=2)

plt.xticks(x, [f"Cycle {i+1}" for i in x], rotation=45)
plt.xlabel("Cycle")
plt.ylabel("Time (seconds)")
plt.title("Task 3 – Pipeline Stage Durations (Stacked Bar Chart)")
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("task3_pipeline_bar_chart.png")
plt.show()