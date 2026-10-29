import random

MIN_VOLTAGE = 11.5

currents = [
    2.0,
    2.1,
    2.2,
    2.3,
    2.4,
    2.5
]


def measure_voltage(current):

    nominal_voltage = 12.1
    internal_resistance = 0.10

    voltage = (
        nominal_voltage
        - current * internal_resistance
    )

    # Simulated hardware fault
    if current >= 2.5:
        voltage -= 0.8

    noise = random.uniform(-0.02, 0.02)

    return voltage + noise


print("\n====================================")
print("       FINE LOAD SWEEP")
print("====================================")

results = []

for current in currents:

    voltage = measure_voltage(current)

    if voltage >= MIN_VOLTAGE:
        result = "PASS"
    else:
        result = "FAIL"

    results.append(
        [current, voltage, result]
    )

    print(
        f"Current: {current:.1f} A | "
        f"Voltage: {voltage:.3f} V | "
        f"Result: {result}"
    )


print("\n====================================")
print("       THRESHOLD RESULT")
print("====================================")

for row in results:

    current = row[0]
    voltage = row[1]
    result = row[2]

    if result == "FAIL":

        print(
            f"First failure detected at "
            f"{current:.1f} A"
        )

        print(
            f"Voltage = {voltage:.3f} V"
        )

        break