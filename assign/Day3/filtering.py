obj =[
    {
        "pid": "1",
        "name": "AC",
        "cost": "27000",
        "brand": "LG",
        "rating": "4",
        "discount": "20",
        "category": "Electronics"
    },
    {
        "pid": "2",
        "name": "Fridge",
        "cost": "4000",
        "brand": "LG",
        "rating": "5",
        "discount": "10",
        "category": "Electronics"
    },
    {
        "pid": "3",
        "name": "WashingMachine",
        "cost": "5000",
        "brand": "Samsung",
        "rating": "4",
        "discount": "15",
        "category": "Electronics"
    },
    {
        "pid": "4",
        "name": "HP202",
        "cost": "50000",
        "brand": "HP",
        "rating": "4",
        "discount": "15",
        "category": "Laptops"
    },
    {
        "pid": "5",
        "name": "le202",
        "cost": "20000",
        "brand": "Lenovo",
        "rating": "5",
        "discount": "15",
        "category": "Laptops"
    }
]
newobj= filter(lambda el: el["brand"] == "LG", obj)
print(type(newobj))
for i in newobj:
    print(i)

newobj = filter(lambda el: el["category"] == "Laptops", obj)
print(type(newobj))
for i in newobj:
    print(i)



