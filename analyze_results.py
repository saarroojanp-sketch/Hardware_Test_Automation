import pandas as pd
import matplotlib.pyplot as plt


# Read automated test results
data = pd.read_csv("load_sweep_results.csv")

print("\n=== LOAD SWEEP RESULTS ===")
print(data)


# Calculate statistics
print("\n=== STATISTICS ===")

print(f"Minimum Voltage: {data['Voltage (V)'].min():.2f} V")
print(f"Maximum Voltage: {data['Voltage (V)'].max():.2f} V")

print(f"Minimum Power: {data['Power (W)'].min():.2f} W")
print(f"Maximum Power: {data['Power (W)'].max():.2f} W")


# Count PASS and FAIL
pass_count = (data["Result"] == "PASS").sum()
fail_count = (data["Result"] == "FAIL").sum()

print(f"\nPASS: {pass_count}")
print(f"FAIL: {fail_count}")


# Voltage vs Current graph
plt.figure()

plt.plot(
    data["Current (A)"],
    data["Voltage (V)"],
    marker="o"
)

plt.xlabel("Current (A)")
plt.ylabel("Voltage (V)")
plt.title("DUT Voltage vs Load Current")

plt.grid(True)

plt.savefig("voltage_vs_current.png")

plt.show()


# Power vs Current graph
plt.figure()

plt.plot(
    data["Current (A)"],
    data["Power (W)"],
    marker="o"
)

plt.xlabel("Current (A)")
plt.ylabel("Power (W)")
plt.title("DUT Power vs Load Current")

plt.grid(True)

plt.savefig("power_vs_current.png")

plt.show()