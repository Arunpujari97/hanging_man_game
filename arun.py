# import random
# word_list = ["apple", "banana", "cherry", "dog", "elephant", "flamingo", "giraffe", "hamburger", "icecream", "jellyfish"]
#
# def choose_random_word():
#     return random.choice(word_list)
#
# def display_word(word, guessed_letters):
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display
#
# def hangman():
#     chosen_word = choose_random_word()
#     guessed_letters = []
#     attempts = 6
#
#     print("Welcome to Hangman!")
#     print(display_word(chosen_word, guessed_letters))
#
#     while attempts > 0:
#         guess = input("Guess a letter: ").lower()
#
#         if len(guess) != 1 or not guess.isalpha():
#             print("Please enter a single letter.")
#             continue
#
#         if guess in guessed_letters:
#             print("You've already guessed that letter.")
#             continue
#
#         guessed_letters.append(guess)
#
#         if guess in chosen_word:
#             print("Correct!")
#         else:
#             attempts -= 1
#             print("Wrong! You have", attempts, "attempts left.")
#
#         word_display = display_word(chosen_word, guessed_letters)
#         print(word_display)
#
#         if "_" not in word_display:
#             print("Congratulations! You guessed the word:", chosen_word)
#             break
#
#     if "_" in word_display:
#         print("Oops! The word was:", chosen_word)
#         print("Better luck next time!")
#
# if __name__ == "__main__":
#     hangman()
