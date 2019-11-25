obj = [
    {"id": "1", "name": "laptop", "cost": "10000", "brand": "sony", "rating": 3, "discount": 70,
     "category": "electronic"},
    {"id": "2", "name": "mobile", "cost": "12000", "brand": "Nokia", "rating": 5, "discount": 20,
     "category": "electronic"},
    {"id": "3", "name": "washing machine", "cost": "15000", "brand": "Samsung", "rating": 4, "discount": 40,
     "category": "electronic"},
    {"id": "4", "name": "mixer grinder", "cost": "13000", "brand": "maharaja", "rating": 3, "discount": 60,
     "category": "electronic"},
]


# for i in obj:
#   # print('{cost}'.format(**i))
def mysort(f):
    if f == 1:
        obj.sort(key=lambda el: el["cost"])
        print(obj)
    elif f == 2:
        obj.sort(key=lambda el: el["cost"], reverse=True)
        print(obj)
    elif f == 3:
        obj.sort(key=lambda el: el["rating"])
        print(obj)
    elif f == 4:
        obj.sort(key=lambda el: el["discount"])
        print(obj)
    elif f == 5:
        obj.sort(key=lambda el: el["discount"], reverse=True)
        print(obj)


mysort(int(input("Enter choice")))
