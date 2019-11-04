sum = 0
for i in str(input()):
    a = int(i)
    if a % 2 == 1:
        sum += a ** 2
print(sum)