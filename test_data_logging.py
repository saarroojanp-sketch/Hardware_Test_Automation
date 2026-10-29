import csv
from measurements import (
    measure_voltage,
    measure_current,
    calculate_power
)


def test_measurement_logging():

    voltage = measure_voltage()
    current = measure_current()
    power = calculate_power(voltage, current)

    voltage_min = 11.5
    voltage_max = 12.5

    current_min = 0.0
    current_max = 3.0

    power_min = 0.0
    power_max = 40.0

    voltage_result = (
        "PASS"
        if voltage_min <= voltage <= voltage_max
        else "FAIL"
    )

    current_result = (
        "PASS"
        if current_min <= current <= current_max
        else "FAIL"
    )

    power_result = (
        "PASS"
        if power_min <= power <= power_max
        else "FAIL"
    )

    with open(
        "test_results.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Parameter",
            "Measured Value",
            "Unit",
            "Minimum",
            "Maximum",
            "Result"
        ])

        writer.writerow([
            "Voltage",
            voltage,
            "V",
            voltage_min,
            voltage_max,
            voltage_result
        ])

        writer.writerow([
            "Current",
            current,
            "A",
            current_min,
            current_max,
            current_result
        ])

        writer.writerow([
            "Power",
            power,
            "W",
            power_min,
            power_max,
            power_result
        ])

    assert voltage_result == "PASS"
    assert current_result == "PASS"
    assert power_result == "PASS"