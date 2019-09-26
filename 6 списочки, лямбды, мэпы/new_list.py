lst = [2, 4, 9, 16, 25]

lst_2 = []
for i in lst:
    lst_2.append(i ** 2)
print(lst_2)

lst_2 = list(map(lambda x: x ** 2, lst))
print(lst_2)

lst_2 = [i ** 2 for i in lst]
print(lst_2)
