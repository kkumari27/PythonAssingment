data = "i am a {0} from {1}"
sub1 = 'string'
lang = 'Python'
print(data.format(sub1, lang))
temp = '''hello {fname} {lname} , welcome to  {city}'''
obj = [{
    'fname': 'Sachin',
    'lname': 'Tendulkar',
    'team': 'mumbai'
},
    {'fname': 'nritika',
     'lname': 'gupta',
     'team': 'bangal'
     },
    {
        'fname': 'kritika',
        'lname': 'kumari',
        'team': 'varanasi'
    }
]


def myfilter(el):
    print("myfilter called for" + el["fname"])
    return el["fname"].startswith == "S"


newobj = filter(myfilter, obj)
print(type(newobj))
for i in newobj:
    print('{fname}'.format(**i))

# obj.sort(key=mysort)
# print(obj)
