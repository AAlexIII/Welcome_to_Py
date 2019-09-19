def fun(a):
    if -2.7 <= a <= 5.7:
        T = True
    return a**2 if T else  4


print(fun(float(input("Any: "))))