import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
end_of_game = False
word_len = len(chosen_word)
lives = 6

print(logo)

display = []
for _ in range(word_len):
    display.append("_")

while not end_of_game:

    guess = input("\nGuess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed '{guess}'.")
    else:
        for i in range(word_len):
            if chosen_word[i] == guess:
                display[i] = chosen_word[i]

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life. {lives} lives remaining.")
        if lives == 0:
            end_of_game = True
            print(f"Oops! You Lose. The word was {chosen_word}.")

    if '_' not in display:
        end_of_game = True
        print(f"Yayy, You Won!")

    print(f"{' '.join(display)}")
    print(stages[lives])




