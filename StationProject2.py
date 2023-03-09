from random import randint


def rolling_dices():
    first_number = randint(1, 6)
    second_number = randint(1, 6)
    print(f'The sum of your dices is {first_number} + {second_number} = {first_number + second_number}')
    return (first_number, second_number)


dices = rolling_dices()
sum = dices[0] + dices[1]
goal = 0


if 4 <= sum <= 10 and sum != 7:

    goal = sum
    print(f"Your goal is {goal} now!\n")
    dices = rolling_dices()

    while dices[0] + dices[1] != goal:
        if dices[0] + dices[1] == 7:
            print("You lost\n")
        dices = rolling_dices()
    print("You won\n")

elif sum == 7 or sum == 11:
    print("You won\n")

elif sum == 2 or sum == 3 or sum == 12:
    print("You lost\n")
