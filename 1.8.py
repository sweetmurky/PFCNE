# functions

def vlans_exist(vlansID):
    vlansList = [1, 10, 20, 30]
    return vlansID in vlansList

vlan = [1, 20, 100, 200]
for vlan in vlan:
    print(vlan, vlans_exist(vlan))





'''
def NetworkDevices():
    print('router1')
    print('router2')

def IPs():
    print('10.1.1.1')
    print('10.10.1.1')

def Both():
    NetworkDevices()
    IPs()


#NetworkDevices()
#IPs()
Both()
'''

