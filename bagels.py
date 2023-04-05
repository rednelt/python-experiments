# I made this when reading The Big Book of Small Python Projects. The first version was made
# based off the game description, then I looked at Al's (better) code and implemented the good stuff.
# I also added sounds for the clues and for when you win or lose.

# "Bagels" - A logic game where you have to guess a secret 3-digit number based on these clues:
# “Pico” when your guess has a correct digit in the wrong place,
# “Fermi” when your guess has a correct digit in the correct place,
# “Bagels” if your guess has no correct digits.
# You have 10 tries.

import random, playsound, os

NUMBER_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f"I thought up a {NUMBER_DIGITS}-digit number that consists of unique digits including zero.")
    print(f"You have {MAX_GUESSES} tries to guess it!")
    print("I will give you the following clues based on your guess:")
    print("“Pico” when your guess has a correct digit in the wrong place,")
    print("“Fermi” when your guess has a correct digit in the correct place,")
    print("“Bagels” if your guess has no correct digits.\n")

    secret_number = get_secret_number()

    guesses = 1

    while guesses <= MAX_GUESSES:
        guess = input(f"Guess #{guesses}: ")
        while not guess.isnumeric() or len(guess) != NUMBER_DIGITS:
            print(f"Please enter a {NUMBER_DIGITS}-digit number.")
            guess = input(f"Guess #{guesses}: ")
            

        if guess == secret_number:
            print("You guessed it!")
            playsound.playsound(os.path.abspath("./sounds/win.mp3"))
            play_again = input("Want to play again? (y/n) ")
            if play_again == "y":
                print()
                main()
            return
        else:
            clues = get_clues(secret_number, guess)
            print(" ".join(clues))
            play_clue_sounds(clues)

            guesses += 1

    print(f"You lose. The secret number was {secret_number}")
    playsound.playsound(os.path.abspath("./sounds/gameover.mp3"))



def get_secret_number():
    digits = list(range(0, 10))
    random.shuffle(digits)

    secret_number = []
    for i in range(NUMBER_DIGITS):
        secret_number.append(str(digits[i]))

    return "".join(secret_number)


def get_clues(secret_number, guess):
    clues = []
    for i in range(len(secret_number)):
        if secret_number[i] == guess[i]:
            clues.append("Fermi")
        elif secret_number[i] in guess:
            clues.append("Pico")
    
    if len(clues) == 0:
        clues.append("Bagels")
    
    return clues


def play_clue_sounds(clues):
    for clue in clues:
        playsound.playsound(os.path.abspath(f"./sounds/{clue.lower()}.wav"))


if __name__ == "__main__":
    main()
