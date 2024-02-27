import random

######################players name
player_name = input("What is your name: ").capitalize()
print(f"{player_name} Welcome to the number guess game!")

while True:
    while True:
        top_range = input("Choose a number: ")
        if top_range.isdigit():
            top_range = int(top_range)
            if top_range < 5:
                print("Number must not be less than 5")
                continue
            else:
                random_number = random.randint(5, top_range)

                guesses = 0

                while True:
                    guesses += 1

                    player_guess = input(f"{player_name} Take a guess: ")
                    if player_guess.isdigit():
                        player_guess = int(player_guess)
                    else:
                        print("Let your Guess be a number!")
                        continue

                    if player_guess == random_number:
                        print(f"{player_name} You won\nYou won on {guesses} guesses")
                        break

                    elif player_guess > random_number:
                        print("You chose above the number!")

                    else:
                        print("You chose below the number!")

                    if guesses == 3:
                        print("You have attempted 3 times")
                        quit()
                break
        else:
            print("Please try again!")
            continue

    play_again = input("Press any key to play again and 'q' to quit: ")
    if play_again == "q":
        quit()

    else:
        continue


