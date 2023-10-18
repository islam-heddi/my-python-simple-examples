a = 0
b = 0
a = int(input("enter a number : "))
b = int(input("enter a number : "))
print("operations are + / * -")
op = input("enter the operation : ")
result = 0
if op == "+" : 
    result = a + b
    print("result : ",result)
elif op == "-" :
    result = a - b
    print("result : ",result)
elif op == "*" :
    result = a * b
    print("result : ",result)
elif op == "/" :
    if b == 0 :
        print("division is impossible !")
    else :
        result = a / b
        print("result : ",result)
