data = "i am a {0} from {1}"
sub1 = 'string'
lang = 'Python'
print(data.format(sub1, lang))
temp = '''hello {fname} {lname} , welcome to  {city}'''
obj = [{
    'fname': 'Sachin',
    'lname': 'Tendulkar',
    'city': 'bangalore'
},
    {'fname': 'Nritika',
     'lname': 'gupta',
     'city': 'bangal'
     },
    {
        'fname': 'kritika',
        'lname': 'kumari',
        'city': 'varanasi'
    }
]


# temp = '''hello {fname} {lname} , welcome to  {city}'''
# for d in obj:
#      dataString=temp.format(**d)
#     print(dataString)
#
# dataString = temp.format(**obj)
# print(dataString)
def mysort(el):
    print("mysort called for"+el["fname"])
    return el["fname"]


obj.sort(key=mysort)
print(obj)
