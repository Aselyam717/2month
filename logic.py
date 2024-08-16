import random
from decouple import config

def guess_the_number_game():
    attempt_str = int(config('attempts'))
    initial_capital = int(config('initial_capital'))
    range_str = config('number_range')
    dash_index = range_str.index('-')
    range_start = int(range_str[:dash_index])
    range_end = int(range_str[dash_index+1:])

    print(f' Диапазон чисел от {range_start}, и до {range_end}, количество попыток {attempt_str}, начальный капитал {initial_capital} ')



    random_number = random.randint(range_start, range_end)



    while attempt_str > 0:

        bet = int(input('Enter your bet:'))

        if bet > initial_capital:
            print(f' Your bet exceeds your capital ({initial_capital}). Try again. ')
            continue

        else:
            print(f' Your bet is accepted. Your current capital: {initial_capital}.')



        guess = int(input(f'Attempt {attempt_str}: Enter your guess ({range_start} - {range_end}): '))

        if guess == random_number:
            initial_capital += bet
            print(f'Congratulations! Your guess is correct. Your current capital is {initial_capital}.')

        elif guess < 1 or guess > 100:
            print('Wrong range. Try again guessing from 1 to 100')

        else:
            initial_capital -= bet
            print(f' Wrong guess. You lost your bet. Your current capital: {initial_capital}.')

        attempt_str -= 1

        if initial_capital <= 0:
            print('Game is over!')
            break
