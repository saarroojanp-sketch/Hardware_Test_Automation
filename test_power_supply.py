from simulated_power_supply import SimulatedPowerSupply


def test_power_supply():

    supply = SimulatedPowerSupply()

    # Configure power supply
    supply.set_voltage(12.0)
    supply.set_current(3.0)

    # Turn output ON
    supply.output_on()

    # Measure
    voltage = supply.measure_voltage()
    current = supply.measure_current()

    power = voltage * current

    print(f"Voltage: {voltage:.2f} V")
    print(f"Current: {current:.2f} A")
    print(f"Power:   {power:.2f} W")

    # Validation
    assert 11.5 <= voltage <= 12.5
    assert 0.0 <= current <= 3.0
    assert power <= 40.0

    # Safety shutdown
    supply.output_off()