import math


def not_pi(k):
    return round(math.pi, k)


print(f"Вот то что вы хотели {not_pi(int(input('Сколько знаков пи вас интересует? ')))}")
