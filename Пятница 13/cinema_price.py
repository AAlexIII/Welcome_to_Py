def find_in_list(list, elem):
    for i in list:
        return i[elem] if elem in i.keys() else ''


film_list = {"Пятница": [{12: 250}, {16: 350}, {20: 450}], "Чемпионы": [{10: 250}, {13: 350}, {16: 350}],
             "Пернатая банда": [{10: 350}, {14: 450}, {18: 450}]}
film = input("Выбрать фильм: ")
day = input("Выбрать день (сегодня, завтра): ")
time = int(input("Выбрать время: "))
ticket_number = int(input("Выбрать количество билетов: "))
print(f"Выбрали фильм: {film} День: {day} Время: {str(time)} Количество билетов: {str(ticket_number)}")
if (film not in film_list.keys()) or (day not in ['завтра', 'сегодня']) or (find_in_list(film_list[film], time) == '') \
        or (ticket_number < 1):
    print("Ошибка ввода.")
else:
    if ticket_number >= 20:
        ticket_number = ticket_number * 0.8
    elif day == 'завтра':
        ticket_number = ticket_number * 0.95
    print(f"К оплате: {str(int(find_in_list(film_list[film], time) * ticket_number))}")
