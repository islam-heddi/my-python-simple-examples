a = int(input("enter the x^2 coef : "))
b = int(input("enter the x coef : "))
c = int(input("enter the last coef : "))
if b*b - 4 * a *c > 0 :
    x1 = ((b*b) - pow(b*b - 4 * a *c , 1/2) /(2*a))
    x2 = ((b*b) + pow(b*b - 4 * a *c , 1/2) /(2*a))
    print("x1 = ",x1," x2 = ",x2)
elif b*b - 4 * a *c == 0 :
    x = (b*b)/(2*a)
    print("x = ",x)
else :
    print("there is no solution")