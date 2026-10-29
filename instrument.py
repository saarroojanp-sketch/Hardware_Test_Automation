class PowerSupply:
    def __init__(self):
        self.output_voltage = 0.0
        self.output_current = 0.0
        self.output_enabled = False

    def set_voltage(self, voltage):
        self.output_voltage = voltage
        print(f"Power Supply: Voltage set to {voltage:.2f} V")

    def set_current_limit(self, current):
        self.output_current = current
        print(f"Power Supply: Current limit set to {current:.2f} A")

    def output_on(self):
        self.output_enabled = True
        print("Power Supply: OUTPUT ON")

    def output_off(self):
        self.output_enabled = False
        print("Power Supply: OUTPUT OFF")


class ElectronicLoad:
    def __init__(self):
        self.load_current = 0.0

    def set_current(self, current):
        self.load_current = current
        print(f"Electronic Load: Current set to {current:.2f} A")

    def output_on(self):
        print("Electronic Load: OUTPUT ON")

    def output_off(self):
        print("Electronic Load: OUTPUT OFF")


class DMM:
    def measure_voltage(self, voltage):
        print(f"DMM: Measuring voltage = {voltage:.2f} V")
        return voltage

    def measure_current(self, current):
        print(f"DMM: Measuring current = {current:.2f} A")
        return current