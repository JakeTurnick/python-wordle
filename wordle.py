import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

words = open('/usr/share/dict/words', 'r')
newWords = []

for word in words:
    if len(word) == 6:
        newWords.append(word)

word = random.choice(newWords).lower()
TEST_WORD = "clear"

curr_wordle = "-----"
attemps = -1  # amount of attempts so far

# Colors are leaking into the input, not sure why
# also if using repeated characters ...
# ... All instances of that character are the same color
# ... ex: word = clear -> rrrrr (all yellow, last should be green)

guess = input(Fore.RESET + "Guess a 5 letter word: ")
while len(guess) != 5:
    guess = input(Fore.RESET + "Word must be 5 characters long: ")

while attemps < 10:
    attemps += 1
    attemp = ""
    guide = ""

    if attemps > 5:
        print(f"You lost! The word was {Fore.RED + word}")
        break

    for char in guess:
        if word.__contains__(char):
            # print(f"{TEST_WORD} contains the letter {char} at {guess.index(char)}")
            if word.index(char) == guess.index(char):
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
    if guess.lower() == word.lower():
        print("you win!\nThe word was - " + Fore.CYAN + guess.lower())
        break

    print(Style.RESET_ALL + f"Attempts remaining: {attemps}/6")
    guess = input(Style.RESET_ALL + guide + "\n")
    while len(guess) != 5:
        guess = input(Fore.RESET + "Word must be 5 characters long: ")
