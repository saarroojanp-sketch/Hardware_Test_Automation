from scpi_instrument import SimulatedInstrument


def test_scpi_instrument():

    instrument = SimulatedInstrument()

    # Reset instrument
    instrument.write("*RST")

    # Ask instrument identification
    identification = instrument.query("*IDN?")

    print(f"Instrument: {identification}")

    # Configure instrument
    instrument.write("VOLT 12")
    instrument.write("CURR 3")

    # Turn output ON
    instrument.write("OUTP ON")

    # Measure values
    voltage = float(instrument.query("MEAS:VOLT?"))
    current = float(instrument.query("MEAS:CURR?"))

    power = voltage * current

    print(f"Measured Voltage: {voltage:.2f} V")
    print(f"Measured Current: {current:.2f} A")
    print(f"Calculated Power: {power:.2f} W")

    # Validation
    assert voltage == 12.0
    assert current == 3.0
    assert power == 36.0

    # Safety shutdown
    instrument.write("OUTP OFF")