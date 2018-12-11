# loops

components = ['nexus', 'csr1000v', 'iosxrv', 'aci']
counter = 1
interface = 1

while interface <= 10:
    print('GigabitEthernet1/{}'.format(interface))
    print('no switchport')
    interface += 1


'''
for item in components:
    print('device is {}'.format(item))
print('#'*80)


while counter <= 5:
    print('counting')
    counter +=1
'''