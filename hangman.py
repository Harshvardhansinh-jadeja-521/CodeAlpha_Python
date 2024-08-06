import random

def get_random_word():
    word_list = ["computer", "programming", "hangman", "software", "hardware"]
    return random.choice(word_list)

def play_hangman():
    word_to_guess = get_random_word()
    guessed_word = ["_"] * len(word_to_guess)
    incorrect_guesses = []
    max_incorrect_guesses = 6

    while True:
        print("\nHangman Game")
        print("Word to guess: " + " ".join(guessed_word))
        print("Incorrect guesses: " + ", ".join(incorrect_guesses))
        print("Remaining guesses: " + str(max_incorrect_guesses - len(incorrect_guesses)))

        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word!")
            break

        if len(incorrect_guesses) >= max_incorrect_guesses:
            print("Game Over! The word was: " + word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in incorrect_guesses or guess in guessed_word:
            print("You've already guessed that letter. Try again.")
            continue

        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            incorrect_guesses.append(guess)

if __name__ == "__main__":
    play_hangman()
