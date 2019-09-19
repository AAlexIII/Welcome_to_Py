class InvailidKod(Exception):
    pass


cost_for_call = {'343': 15, '381': 18, '473': 13, '485': 11}
kod = input("Телефон: ")[1:4]
if kod not in cost_for_call.keys():
    raise InvailidKod(kod + "  номера нет в списке")
time = float(input("Введите время разговора (мин.сек): "))
print("Стоимость: ", cost_for_call[kod] * (int(time) + (time % 1) / 0.6))
