import random

def guess(x):
    random_number = random.randint(1,x)
    num = 0
    while num != random_number:

        try:
            num = int(input(f'Guess a number between 1 and {x}, (both inclusive): '))
            if num < random_number:
                print(f'Oops, too low.')
            elif num > random_number:
                print(f'Oops, too high.')

        except ValueError:
            print('ValueError, Please enter a whole number.')

    print(f'Congrats! {random_number} is the right guess!')
            
guess(3)

#----------------Note------------------------
#random.randint(x, y) → includes both x and y.
#range(x, y) → includes x, but excludes y.