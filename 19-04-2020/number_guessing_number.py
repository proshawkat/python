winning_number = 43
guess = 1
number = int(input('guess a number between 1 to 100 : '))
game_over = False

while not game_over:
    if number == winning_number:
        print("You win, and you guessed this number in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print('Too low')
        else:
            print('Too high')
        guess += 1
        number = int(input('guess again :'))