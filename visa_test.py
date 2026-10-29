import pyvisa

rm = pyvisa.ResourceManager()

print("VISA Resource Manager:")
print(rm)

print("\nConnected VISA Instruments:")

resources = rm.list_resources()

if resources:
    for resource in resources:
        print(resource)
else:
    print("No VISA instruments detected.")