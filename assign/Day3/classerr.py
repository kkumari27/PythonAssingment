class NameNotFound(Exception):
    def __init__(self, msg="name not found"):
        Exception.__init__(self, msg)

    dict= {
        "sachin": "icc",
        "saurabh": "bcci"
    }
try:

    n1=input("enter the username: ")
    n2=input("enter the password:")

    if n1 in dict.keys:
        raise NameNotFound
    print("invalid keys")

    if n2 in dict.values:
        raise NameNotFound
    print("invalid value")
except NameNotFound as e:
    print(e)



