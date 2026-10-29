import pytest


@pytest.mark.parametrize(
    "voltage, current",
    [
        (12.05, 0.5),
        (12.02, 1.0),
        (11.98, 1.5),
        (11.95, 2.0),
    ]
)
def test_power_measurement(voltage, current):

    minimum_voltage = 11.5
    maximum_voltage = 12.5

    minimum_current = 0.0
    maximum_current = 3.0

    measured_power = voltage * current

    minimum_power = 0.0
    maximum_power = 40.0

    assert minimum_voltage <= voltage <= maximum_voltage
    assert minimum_current <= current <= maximum_current
    assert minimum_power <= measured_power <= maximum_power