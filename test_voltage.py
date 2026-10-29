def test_voltage():
    measured_voltage = 12.05

    minimum_voltage = 11.5
    maximum_voltage = 12.5

    assert minimum_voltage <= measured_voltage <= maximum_voltage
    