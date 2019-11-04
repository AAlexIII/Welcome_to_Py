pr = '''Простой todo: 
    1. Добавить задачу.
    2. Вывести список задач.
    3. Выход.'''
print(pr)
k = input('Укажите число: ')
list=[]
while k != '3':
    if k == '1':
        z = input()
        c = input()
        t = input()
        list.append((z,c,t))
    if k == '2':
        for i in list:
            print(f'Задача: {i[0]}  Категория: {i[1]}  Дата: {i[2]}')
    print(pr)
    k = input('Укажите число: ')
