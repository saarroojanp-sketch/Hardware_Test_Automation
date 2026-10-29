import csv

from config_loader import load_config
from dut_model import SimulatedDUT
from failure_analysis import analyze_measurement


def generate_current_points(start, stop, step):

    currents = []

    current = start

    while current <= stop + 0.0001:

        currents.append(round(current, 2))

        current += step

    return currents


config = load_config()

start = config["test_plan"]["fine_sweep"]["start"]
stop = config["test_plan"]["fine_sweep"]["stop"]
step = config["test_plan"]["fine_sweep"]["step"]

currents = generate_current_points(
    start,
    stop,
    step
)

dut = SimulatedDUT()

results = []

print("\n====================================")
print("       FINE SWEEP VALIDATION")
print("====================================")


for current in currents:

    voltage = dut.measure(current)

    measured_current = current

    power = voltage * measured_current

    result, failures = analyze_measurement(
        voltage,
        measured_current,
        power,
        config
    )

    print(
        f"\nCurrent : {current:.2f} A"
    )

    print(
        f"Voltage : {voltage:.3f} V"
    )

    print(
        f"Power   : {power:.3f} W"
    )

    print(
        f"Result  : {result}"
    )

    if failures:

        for failure in failures:

            print(
                f"Failure : "
                f"{failure['failure_type']} | "
                f"Measured = {failure['measured']:.3f} | "
                f"Limit = {failure['limit']:.3f}"
            )

    results.append({
        "current": measured_current,
        "voltage": voltage,
        "power": power,
        "result": result,
        "failures": failures
    })


# ====================================
# SAVE CSV
# ====================================

with open(
    "fine_sweep_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Test Point",
        "Current (A)",
        "Voltage (V)",
        "Power (W)",
        "Result",
        "Failure Type",
        "Deviation (V)"
    ])

    for index, result in enumerate(
        results,
        start=1
    ):

        if result["failures"]:

            failure_type = "; ".join(
                failure["failure_type"]
                for failure in result["failures"]
            )

            deviation = "; ".join(
                f"{failure['measured'] - failure['limit']:.3f}"
                for failure in result["failures"]
            )

        else:

            failure_type = "NONE"

            deviation = "0.000"


        writer.writerow([
            index,
            result["current"],
            result["voltage"],
            result["power"],
            result["result"],
            failure_type,
            deviation
        ])


print("\n====================================")
print("       FINE SWEEP COMPLETE")
print("====================================")

print(
    "\nResults saved to:"
)

print(
    "fine_sweep_results.csv"
)