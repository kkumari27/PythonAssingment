import re

x = input("enter the mobile no.")

pattern = '^[0-9]{10}$'
match = re.search(pattern, x)

print(re.search(pattern, x))
if re.search(pattern, x):
    print('found a match')
else:
    print('no match')
