import random
from colorama import Fore, Back

TEST_WORD = "clear"

curr_wordle = "-----"
attemps = -1  # amount of attempts so far


guess = input(Fore.RESET + "Guess a 5 letter word: ")
while len(guess) != 5:
    guess = input(Fore.RESET + "Word must be 5 characters long: ")

while attemps < 10:
    attemps += 1
    attemp = ""
    guide = ""

    if attemps > 5:
        print(f"You lost! The word was {Fore.RED + TEST_WORD}")
        break

    for char in guess:
        if TEST_WORD.__contains__(char):
            # print(f"{TEST_WORD} contains the letter {char} at {guess.index(char)}")
            if TEST_WORD.index(char) == guess.index(char):
                # print(f"{char} is in the right place")
                # print green
                attemp += (Fore.GREEN + char)
                guide += (Fore.GREEN + char)
            # print yellow
            else:
                attemp += (Fore.YELLOW + char)
                guide += (Fore.YELLOW + char)
        # add character no style
        else:
            attemp += (Fore.RESET + char)
            guide += (Fore.RESET + "-")
    Fore.RESET
    # print("attemp: ", attemp, " word: ", TEST_WORD)
    if guess.lower() == TEST_WORD.lower():
        print("you win!\nThe word was - " + Fore.CYAN + guess.lower())
        break

    print(f"Attempts remaining: {attemps}/6")
    guess = input(Fore.RESET + guide + "\n")
    while len(guess) != 5:
        guess = input(Fore.RESET + "Word must be 5 characters long: ")
