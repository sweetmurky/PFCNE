# 1.tmp
numbers2 = {'1', '2', '3', '4'}
numbers3 = {1, 2, 3, 4}

print(type(numbers2))
print(type(numbers3))
"""
ipaddress = "111.2.3.4"
device1 = "DataCenter Router"

print(device1.find('router'))
print(device1.upper())


print(ipaddress)
print(ipaddress[0:4])
split_ipaddress = ipaddress.split('.')
print(set(split_ipaddress))


print('10' in ipaddress)
print(ipaddress.startswith('10'))
print(ipaddress.startswith('20'))


banner = "Notice: This device is for authorized use only \n\n        Logins to this device are monitored"

print(banner)


devices = {'host': 'myhost', 'ip': '10.1.1.1'}
device_list = ['asa', 'isr', 'catalyst', 'asr']
interface_id = 1

print(devices)
print(devices.keys())
device_list.sort()
for item in device_list:
    print('Device type is: {}'.format(item))
print('#' * 50)
while interface_id <= 5:
    print('Ethernet1/{}'.format(interface_id))
    interface_id += 1
print('#' * 50)


def get_vlans():
    vlan_list = [1, 5, 10, 20]
    return vlan_list

vlans = get_vlans()
print(vlans)
print('#' * 50)


def vlan_exists(vlan_id):
    vlan_list = [1, 5, 10, 20]
    return vlan_id in vlan_list


# test if vlan exists, pass value 99
print(vlan_exists(20))

"""
