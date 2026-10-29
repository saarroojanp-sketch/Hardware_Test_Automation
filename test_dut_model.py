from dut_model import SimulatedDUT


def test_dut_measurement():

    dut = SimulatedDUT()

    voltage = dut.measure(2.0)

    print(f"Measured Voltage: {voltage:.3f} V")

    assert 11.5 <= voltage <= 12.5