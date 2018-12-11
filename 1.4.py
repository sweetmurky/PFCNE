# sets
# book says do this:
# nexus = set(['9504', '9508', '9516'])
#catalyst = set(['2960', '3560', '3580'])

# following accomplishes same, without pycharm warning:
nexus = {'9504', '9508', '9516'}
catalyst = {'2960', '3560', '3580'}
devices = nexus | catalyst
# datacenter = {'9508', '9516', '9504'}
datacenter = devices - catalyst
# create ORDERED copy of devices SET
devices_list = list(devices)
print(type(nexus))
print(type(catalyst))
print('#'*80)
print(devices)
print(type(devices))
print(type(devices_list))
devices_list.sort()
print(devices_list)
print('#'*80)
devices.add('666')
devices = nexus | catalyst
print(devices)
print(devices_list)
print('#'*80)
print('datacenter is ' + str(type(datacenter)))
print(datacenter)

