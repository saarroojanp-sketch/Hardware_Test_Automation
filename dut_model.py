import random

class SimulatedDUT:

    def __init__(self):
        self.nominal_voltage = 12.1
        self.internal_resistance = 0.10

    def measure(self, current):

        voltage = (
            self.nominal_voltage
            - (current * self.internal_resistance)
        )

        # Simulated hardware fault
        if current >= 2.5:
            voltage -= 0.8

        noise = random.uniform(-0.02, 0.02)

        voltage = voltage + noise

        return voltage