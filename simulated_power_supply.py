from instrument_interface import InstrumentInterface


class SimulatedPowerSupply(InstrumentInterface):

    def __init__(self):
        self.voltage = 0.0
        self.current = 0.0
        self.output_enabled = False

    def set_voltage(self, voltage):
        self.voltage = voltage
        print(f"SIM: VOLT {voltage:.2f}")

    def set_current(self, current):
        self.current = current
        print(f"SIM: CURR {current:.2f}")

    def output_on(self):
        self.output_enabled = True
        print("SIM: OUTP ON")

    def output_off(self):
        self.output_enabled = False
        print("SIM: OUTP OFF")

    def measure_voltage(self):
        print("SIM: MEAS:VOLT?")
        return self.voltage

    def measure_current(self):
        print("SIM: MEAS:CURR?")
        return self.current