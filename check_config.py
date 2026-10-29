from config_loader import load_config


config = load_config()

print("Voltage limits:")
print(config["voltage"]["min"])
print(config["voltage"]["max"])

print("\nCurrent limits:")
print(config["current"]["min"])
print(config["current"]["max"])

print("\nPower limits:")
print(config["power"]["min"])
print(config["power"]["max"])