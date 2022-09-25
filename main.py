import random as rdm

number_guess = rdm.randint(0, 100)
counter = 1
running = True
while running:
    player_guess = int(input("Enter your guess to mystery number: "))

    if number_guess > player_guess:
        print("Your guess is too low. Try again\n")
    elif number_guess < player_guess:
        print("Your guess is too high. Try again\n")
    elif number_guess == player_guess:
        print("Your guess is correct!")
        print("Total Guess: ", counter)
        running = False
    counter += 1

