import random


def win_or_lose(a, b):
    """
    :param a: ваше число
    :param b: рандом
    :return: то что надо =)
    """
    if a == b:
        return "Win"
    else:
        if a > b:
            return "Слишком много"
        else:
            return "Слишком мало"


print(win_or_lose(int(input("Введите число ")), random.randint(1, 4)))

