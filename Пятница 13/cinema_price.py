# Не готово ещё

film_list = {"Пятница":[{12:250},{16:350},{20:450}],"Чемпионы":[{10:250},{13:350},{16:350}],"Пернатая банда": [{10:350},
{14:450},{18:450}]}
film = input('Выбрать фильм: ')
day = input('Выбрать день (сегодня, завтра): ')
time = int(input('Выбрать время: '))
tiket_number =int( input('Выбрать количество билетов: '))
print('Выбрали фильм: ' + film + ' День: ' + day +' Время: ' + str(time) + 'Количество билетов: '+ str(tiket_number))
if (film not in film_list.keys()) or (day not in ['завтра', 'сегодня']) or (time not in film_list[film].keys()) or tiket_number < 1:
    print('Ошибка ввода.')
else:
    if tiket_number >= 20:
        tiket_number = tiket_number * 0.8
    elif film == 'завтра':
        tiket_number = tiket_number * 0.95
    print("К оплате: " + film_list[film][time]*tiket_number)
