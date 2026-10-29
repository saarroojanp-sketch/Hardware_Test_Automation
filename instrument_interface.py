class InstrumentInterface:

    def set_voltage(self, voltage):
        raise NotImplementedError

    def set_current(self, current):
        raise NotImplementedError

    def output_on(self):
        raise NotImplementedError

    def output_off(self):
        raise NotImplementedError

    def measure_voltage(self):
        raise NotImplementedError

    def measure_current(self):
        raise NotImplementedError