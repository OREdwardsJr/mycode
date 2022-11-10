def guess_destination():
    correct_answer = False
    hints = ["It is located in eastern Asia", "It is an island", "It houses Mt. Fuji"]
    i = 0
    answer = "Japan"

    print("Guess which country I'm visiting for my next trip!")

    while (correct_answer == False) & (i < len(hints)):
        print(f"You have {len(hints) - i} guesses left")

        guess = input("Which country do you think I'm visiting").title()

        correct_answer = (guess == answer)

        if correct_answer:
            break

        print(f"Sorry that's wrong! Here's a hint: {hints[i]}")

        i += 1

    if correct_answer:
        print(f"Great Job! I'm visinting {answer}!")
    else:
        print(f"Sorry, you ran out of guesses. The correct answer is {answer}")


def guess_how_many_places():
    answered = False
    count = 32

    while (not answered):
        try:
            guess = int(input("How many countries do you think I've visited? (Enter -1 to quit"))

            if (guess == -1) or (guess == count):
                message = "You guessed correctly" if (guess == count) else  "You chose to quit"
                break
            elif (guess < count):
                print("That's too low! Aim higher :)")
            else:
                print("I wish! That's too high! Aim lower :)")

            answered = (guess == count)  
        except:
            print("Invalid input. Only numbers are accepted")

    print(f"{message}! I've visited {count} countries so far! Thanks for playing! Bye :)")


def guess_places_ive_visited():
    visited_countries = {"Peru", "Costa Rica", "Mexico", "Canada", "Germany", "Luxembourg","England", "Ireland", "France", "Greece", "Italy", "Spain"}
    list_of_countries = {"Peru", "Costa Rica", "Mexico", "Canda", "Germany", "Luxembourg", "England", "Ireland", "France", "Greece", "Italy", "Spain", "Egypt", "Chile", "Brazil", "Jamaica", "Colombia", "India", "Switzerland"}    
    user_score = 0

    while list_of_countries:
        country = list_of_countries.pop()
        visited = (country in visited_countries)
        guess = None

        while (guess not in [1, 2]):
            try:
                guess = int(input(f"Do you think I've visited: {country}? (Enter 1 for yes, 2 for no)"))
            except:
                print("Invalid input, please enter 1 or 2")

        if (guess == visited):
            print("Correct guess!")
            user_score += 1
        else:
            print("Incorrect guess")

        print(f"Your score is {user_score} and you have {len(list_of_countries)} more rounds.")
        new_round = input("Continue? Enter 'end' to quit").lower()

        if (new_round == "end"):
            list_of_countries.clear()

    print(f"Thank you for playing you guessed correctly {user_score} times") 


if __name__ == "__main__":
    guess_destination()
    guess_how_many_places()
    guess_places_ive_visited()
