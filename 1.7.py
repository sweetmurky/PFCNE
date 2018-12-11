# regex

import re
interface = ' Hardware is Ethernet SVI, address is c84c.75b4.19ff (bia c84c.75b4.19ff)'
mac = re.search('c84c', interface)
mac_full = re.search('c84c..........', interface)
print("There is a device with OUI: ")
print(mac.group(0))
print('#'*80)
print("The full mac addr is: ")
print(mac_full.group(0))

