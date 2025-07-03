import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters, wrong_letters):
    """Displays the game state and guessing progress."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(f"Word: {display_word}")
    print("\n")

def play_game():

    secret_word = get_random_word()
    guessed_letters = []
    wrong_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")
    print(f"Secret word selected: {secret_word}")# for testing, later remove this line

    while True:
        display_game_state(mistakes, secret_word, guessed_letters, wrong_letters)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not ('a' <= guess <= 'z'):
            print("Please enter only one letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good job! {guess} is in the word.!")
        else:
            print(f"Sorry, {guess} is not in the word.")
            wrong_letters.append(guess)
            mistakes += 1

        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break
        if all_guessed:
            display_game_state(mistakes, secret_word, guessed_letters, wrong_letters)
            print("You saved the snowman! YOU WIN!!!")
            break

        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters, wrong_letters)
            print("-"*20)
            print("The snowman melted! YOU LOSE!!!")
            print(f"Your letters where {wrong_letters}")
            print(f"The secret word was: {secret_word}")
            print("-" * 20)
            break

(play_game())
