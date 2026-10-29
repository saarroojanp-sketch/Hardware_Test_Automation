import pyvisa


class RealVisaPowerSupply:

    def __init__(self, resource_name):
        self.rm = pyvisa.ResourceManager()
        self.instrument = self.rm.open_resource(resource_name)

    def identify(self):
        return self.instrument.query("*IDN?")

    def close(self):
        self.instrument.close()
        self.rm.close()