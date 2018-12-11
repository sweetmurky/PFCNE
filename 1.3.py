# tuples

credentials = ('hostname', 'username', 'password')
print(type(credentials))
print(credentials.count('hostname'))
copy_credentials = list(credentials)
print(type(copy_credentials))
print(copy_credentials)
copy_credentials.pop()
print(copy_credentials)
print('#'* 80)
device, user, pw = credentials
print(type(credentials))
print(credentials)