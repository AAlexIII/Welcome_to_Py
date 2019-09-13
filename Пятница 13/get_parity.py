def odd_check(a):
    return "Odd" if ((int(a) % 2) == 1)  else "Even"


print(odd_check(input("Is it odd or even? ")))