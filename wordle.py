import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

TEST_WORD = "apple"
words = open('/usr/share/dict/words', 'r')
newWords = []

for word in words:
    if len(word) == 6:
        newWords.append(word)
words.close()

word = random.choice(newWords).lower().strip()
word = TEST_WORD
print("Hint - " + word)


curr_wordle = "-----"
attemps = -1  # amount of attempts so far

# Colors are leaking into the input, not sure why
# also if using repeated characters ...
# ... All instances of that character are the same color
# ... ex: word = clear -> rrrrr (all yellow, last should be green)
# print("Hint -", word)

guess = input(Fore.RESET + "Guess a 5 letter word: ")
while len(guess) != 5:
    guess = input(Fore.RESET + "Word must be 5 characters long: ")


while attemps < 10:
    attemps += 1
    attemp = ""
    guide = ""
    Style.RESET_ALL

    if attemps > 6:
        Fore.RESET
        print(f"You lost! The word was {Fore.RED + word}")
        break

# the issue is the index is checked by the first instance of the letter
    # for char in guess:
    #     if word.__contains__(char):
    #         # print(f"{TEST_WORD} contains the letter {char} at {guess.index(char)}")
    #         if word.index(char) == guess.index(char):
    #             # print(f"{char} is in the right place")
    #             # print green
    #             attemp += (Fore.GREEN + char)
    #             guide += (Fore.GREEN + char)
    #             Style.RESET_ALL
    #         # print yellow
    #         else:
    #             attemp += (Fore.YELLOW + char)
    #             guide += (Fore.YELLOW + char)
    #             Style.RESET_ALL
    #     # add character no style
    #     else:
    #         attemp += (Fore.RESET + char)
    #         guide += (Fore.RESET + "-")
    #         guide_check[guess.index(char)] = ""
    # Fore.RESET

    for i in range(0, 5):
        if word.__contains__(guess[i]):
            if word[i] == guess[i]:
                attemp += (Fore.GREEN + guess[i])
                guide += (Fore.GREEN + guess[i])
                Style.RESET_ALL
            # print yellow
            else:
                attemp += (Fore.YELLOW + guess[i])
                guide += (Fore.YELLOW + guess[i])
                Style.RESET_ALL
        # add character no style
        else:
            attemp += (Fore.RESET + guess[i])
            guide += (Fore.RESET + "-")
    Fore.RESET

    if guess.lower() == word.lower():
        print("you win!\nThe word was - " + Fore.CYAN + guess.lower())
        break

    print(Fore.RESET + f"Attempts remaining: {attemps}/6")
    guess = input(Fore.RESET + guide + "\n")
    while len(guess) != 5:
        guess = input(Fore.RESET + "Word must be 5 characters long: ")

    # guess = input(Fore.RESET + "Guess a 5 letter word: ")
    # while len(guess) != 5:
    #     guess = input(Fore.RESET + "Word must be 5 characters long: ")
