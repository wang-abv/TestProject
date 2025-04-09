import random

def hangman():
    words = ["python", "programming", "hangman"]
    word = random.choice(words)
    guesses = []
    attempts = 6

    while attempts > 0:
        display = ''.join([letter if letter in guesses else '_' for letter in word])
        print(display)
        print(f"Guesses left: {attempts}")
        guess = input("Enter your guess: ").lower()
        if guess in word and guess not in guesses:
            guesses.append(guess)
        elif guess in guesses:
            print("You already guessed that letter!")
        else:
            attempts -= 1
            print("Incorrect guess!")

        if display == word:
            print("Congratulations! You've won!")
            break
        if attempts == 0:
            print(f"Game over! The word was {word}")

hangman()
