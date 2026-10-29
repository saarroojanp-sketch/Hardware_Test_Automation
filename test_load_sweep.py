import csv


def simulate_measurement(current):
    """
    Simulate a DUT voltage measurement.

    As current increases, the DUT voltage
    drops slightly due to load.
    """

    voltage = 12.10 - (current * 0.10)

    return voltage


def test_load_sweep():

    # Load points to test
    load_currents = [
        0.5,
        1.0,
        1.5,
        2.0,
        2.5,
        3.0
    ]

    # Voltage limits
    minimum_voltage = 11.5
    maximum_voltage = 12.5

    # Current limits
    minimum_current = 0.0
    maximum_current = 3.0

    # Power limit
    maximum_power = 40.0

    results = []

    for current in load_currents:

        # Measure voltage
        voltage = simulate_measurement(current)

        # Calculate power
        power = voltage * current

        # Check voltage
        voltage_pass = (
            minimum_voltage
            <= voltage
            <= maximum_voltage
        )

        # Check current
        current_pass = (
            minimum_current
            <= current
            <= maximum_current
        )

        # Check power
        power_pass = (
            0.0
            <= power
            <= maximum_power
        )

        # Overall result
        if voltage_pass and current_pass and power_pass:
            result = "PASS"
        else:
            result = "FAIL"

        results.append([
            current,
            voltage,
            power,
            result
        ])

    # Save results
    with open(
        "load_sweep_results.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Current (A)",
            "Voltage (V)",
            "Power (W)",
            "Result"
        ])

        writer.writerows(results)

    # Make sure every test point passed
    for result in results:
        assert result[3] == "PASS"