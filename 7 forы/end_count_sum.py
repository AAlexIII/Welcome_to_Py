sum = 0
s = input("Введите число или cтоп для выхода: ")
while s != 'стоп':
    if not s.isdigit():
        print('fail')
    else:
        sum += int(s)
    s = input("Введите число или cтоп для выхода: ")
print(f"Cумма: {sum}")
