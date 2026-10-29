from instrument import PowerSupply, ElectronicLoad, DMM


def test_instrument_setup():

    power_supply = PowerSupply()
    electronic_load = ElectronicLoad()
    dmm = DMM()

    # Configure power supply
    power_supply.set_voltage(12.0)
    power_supply.set_current_limit(3.0)
    power_supply.output_on()

    # Configure electronic load
    electronic_load.set_current(2.0)
    electronic_load.output_on()

    # Simulated measurement
    measured_voltage = 11.9
    measured_current = 2.0

    voltage = dmm.measure_voltage(measured_voltage)
    current = dmm.measure_current(measured_current)

    power = voltage * current

    print(f"\nMeasured Voltage: {voltage:.2f} V")
    print(f"Measured Current: {current:.2f} A")
    print(f"Calculated Power: {power:.2f} W")

    # Validation
    assert 11.5 <= voltage <= 12.5
    assert 0.0 <= current <= 3.0
    assert 0.0 <= power <= 40.0

    # Safety shutdown
    electronic_load.output_off()
    power_supply.output_off()