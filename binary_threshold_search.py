from dut_model import SimulatedDUT
from config_loader import load_config
from failure_analysis import analyze_measurement


config = load_config()

dut = SimulatedDUT()

# Known PASS and FAIL points
low = 2.40
high = 2.50

print("\n====================================")
print("      BINARY THRESHOLD SEARCH")
print("====================================")

print(f"Known PASS point : {low:.2f} A")
print(f"Known FAIL point : {high:.2f} A")

iteration = 0

while (high - low) > 0.01:

    iteration += 1

    # Find middle point
    middle = (low + high) / 2

    voltage = dut.measure(middle)

    current = middle
    power = voltage * current

    result, failures = analyze_measurement(
        voltage,
        current,
        power,
        config
    )

    print(
        f"\nIteration {iteration}"
        f" | Current = {current:.3f} A"
        f" | Voltage = {voltage:.3f} V"
        f" | Result = {result}"
    )

    if result == "PASS":
        low = middle

    else:
        high = middle


print("\n====================================")
print("      BINARY SEARCH COMPLETE")
print("====================================")

print(f"Last PASS current : {low:.3f} A")
print(f"First FAIL current: {high:.3f} A")

print(
    f"Failure threshold is between "
    f"{low:.3f} A and {high:.3f} A"
)