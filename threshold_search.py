from dut_model import SimulatedDUT
from config_loader import load_config
from failure_analysis import analyze_measurement


config = load_config()

dut = SimulatedDUT()

minimum_voltage = config["limits"]["voltage"]["min"]

low = 2.40
high = 2.50

step = 0.01


print("\n====================================")
print("       AUTOMATIC THRESHOLD SEARCH")
print("====================================")

print(f"Starting PASS point : {low:.2f} A")
print(f"Starting FAIL point : {high:.2f} A")
print(f"Search resolution   : {step:.2f} A")


current = low

while current <= high + 0.0001:

    voltage = dut.measure(current)

    power = voltage * current

    result, failures = analyze_measurement(
        voltage,
        current,
        power,
        config
    )

    print(
        f"\nCurrent = {current:.2f} A"
        f" | Voltage = {voltage:.3f} V"
        f" | Result = {result}"
    )

    if result == "FAIL":

        print(
            f"\nFIRST FAILURE FOUND"
        )

        print(
            f"Failure Current : {current:.2f} A"
        )

        print(
            f"Voltage         : {voltage:.3f} V"
        )

        for failure in failures:

            print(
                f"Failure Type    : "
                f"{failure['failure_type']}"
            )

        break

    current += step


print("\n====================================")
print("       THRESHOLD SEARCH COMPLETE")
print("====================================")