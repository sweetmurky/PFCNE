# Dictionaries

device = {'hostname': 'router1', 'OS': 'v15.5'}
device2 = {}
device3 = {'key': 'value'}
print(type(device))
print('#' * 80)
print(device.keys())
print(device['OS'])
print(device.get('OS'))
print(device['hostname'])

device.update({'OS': 'v15.6'})
print(device)

print('#' * 80)
print(device2)
print(device3)

print(device.keys())
print(device.values())
print(device.items())
print('#' * 80)
device.pop('OS')
print(device)
print(device.get("hostname"))
