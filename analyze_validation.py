import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("detailed_validation_results.csv")

print("\n=== VALIDATION DATA ===")
print(data)

print("\n=== SUMMARY ===")

print(f"Total Test Points : {len(data)}")
print(f"PASS              : {(data['Result'] == 'PASS').sum()}")
print(f"FAIL              : {(data['Result'] == 'FAIL').sum()}")

print(
    f"Minimum Voltage   : "
    f"{data['Voltage (V)'].min():.3f} V"
)

print(
    f"Maximum Voltage   : "
    f"{data['Voltage (V)'].max():.3f} V"
)

print(
    f"Minimum Duration  : "
    f"{data['Duration (s)'].min():.6f} s"
)

print(
    f"Maximum Duration  : "
    f"{data['Duration (s)'].max():.6f} s"
)


# -----------------------------
# VOLTAGE VS CURRENT
# -----------------------------

plt.figure()

plt.plot(
    data["Current (A)"],
    data["Voltage (V)"],
    marker="o"
)

plt.xlabel("Load Current (A)")
plt.ylabel("Measured Voltage (V)")
plt.title("DUT Voltage vs Load Current")

plt.grid(True)

plt.savefig("validation_voltage_vs_current.png")

plt.show()