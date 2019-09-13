# Не готово ещё

film_list = {"Пятница":[12,16,20],"Чемпионы":[10,13,16],"Пернатая банда": [10,14,18]}
film = input('Выбрать фильм: ')
day = input('Выбрать день (сегодня, завтра): ')
time = input('Выбрать время: ')
tiket_number = input('Выбрать количество билетов: ')
print('Выбрали фильм: ' + film + ' День: ' + day +' Время: ' + time + 'Количество билетов: '+ tiket_number)
if (film not in film_list.keys()) or (day not in ['завтра', 'сегодня']) or (time not in film_list[film]) or tiket_number < 1:
    print('Ошибка ввода.')
else:
    if film == 'завтра':
