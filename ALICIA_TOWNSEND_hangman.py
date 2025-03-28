import random, ALICIA_TOWNSEND_hangman_stages, sys

def select_word(words):
    return random.choice(words)

def print_secret_word(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(" {} ".format(letter), end="") 
        else:
            print(" _ ", end="")
    print("\n")

def is_guess_in_secret_word(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print("Unable to continue, only use one letter")
        sys.exit()
    else:
        if guess in secret_word:
            return True
        else:
            return False

def get_unique_letters(word):
    return "".join(set(word))

words = ["python", "cobra", "viper", "snake", "anaconda"]
remaining_attempts = 11
guessed_letters = ""

print("Let's play Hangman! Can you guess my word? xD")
secret_word = select_word(words)

while remaining_attempts > 0 and len(guessed_letters) < len(get_unique_letters(secret_word)):
    guess = input("Guess a letter: ")
    guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

    if guess_in_secret_word:
        if guess in guessed_letters:
            print("You've already guessed the letter '{}'!".format(guess))
        else:
            print("Correct!\n The letter '{}' is in the word".format(guess))
            guessed_letters += guess
    else:
        print("Incorrect!\n The letter '{}' is not in the word".format(guess))
        remaining_attempts -= 1

    print(ALICIA_TOWNSEND_hangman_stages.get_hangman_stage(remaining_attempts))
    print("\n{} attempts left!\n".format(remaining_attempts))
    print_secret_word(secret_word, guessed_letters)
    
if len(guessed_letters)  == len(get_unique_letters(secret_word)):
    print("Amazing job! You guessed my word correctly!\n")
else:
    print("Oopsie!! Better luck next time! :'C\n")
