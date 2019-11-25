#Anonymous function
#Inline function
#lambda function

# rule1:function should contain 1 line
# rele2:that 1 line should be return statement

# def sayhi(n1,n2):
    # return "hi "+n1+" "+n2

data=(lambda n1,n2:"hi "+n1+" "+n2)
print(type(data))
print(data("A","B"))
print(data("C","D"))
# print(data("A","B"))