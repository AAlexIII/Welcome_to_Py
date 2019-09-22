import random


worlds = ['самовар', 'весна', 'лето']
answer = worlds[random.randint(0, len(worlds)-1)]
rand_world = list(answer)
rand_letter = rand_world[random.randint(0, len(rand_world)-1)]
rand_world[rand_world.index(rand_letter)] = '?'
print(''.join(rand_world))
print('Победа!' if rand_letter == input('Введите букву: ') else 'Увы! Попробуйте в другой раз.')
print(f'Слово: {answer}')

