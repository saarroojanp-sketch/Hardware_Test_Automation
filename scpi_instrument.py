class SimulatedInstrument:

    def __init__(self):
        self.voltage = 0.0
        self.current = 0.0
        self.output = False

    def write(self, command):

        print(f">>> SCPI: {command}")

        command = command.upper()

        if command == "*RST":
            self.voltage = 0.0
            self.current = 0.0
            self.output = False

        elif command.startswith("VOLT"):
            value = float(command.split()[1])
            self.voltage = value

        elif command.startswith("CURR"):
            value = float(command.split()[1])
            self.current = value

        elif command == "OUTP ON":
            self.output = True

        elif command == "OUTP OFF":
            self.output = False

    def query(self, command):

        print(f">>> SCPI QUERY: {command}")

        command = command.upper()

        if command == "*IDN?":
            return "SIMULATED,DUT-POWER-SUPPLY,001,1.0"

        elif command == "MEAS:VOLT?":
            return str(self.voltage)

        elif command == "MEAS:CURR?":
            return str(self.current)

        return "UNKNOWN COMMAND"