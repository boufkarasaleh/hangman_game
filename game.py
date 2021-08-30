# Hangman Game
import random
import needs

print(needs.logo)
# Chosing a random word
chosen_word = random.choice(needs.words)

print(chosen_word)
lives = 6
# Chosen_word letters in list of blanks
display = []
for item in range(len(chosen_word)):
    display += "_"

end_of_game = False
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    # If you guessed the same letter twice
    if user_guess in display:
        print(f"You've already guessed {user_guess}")

    # Checking for a guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if user_guess == letter:
            display[position] = letter
    print(display)

    # If there is no more blanks in display the you win
    if "_" not in display:
        end_of_game = True
        print("you win!")

    # If lives goes down to 0 then you lose
    if user_guess not in chosen_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")

        # If lives goes down to 0 then you lose
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    
    # Printing the display as a string 
    print(f"{' '.join(display)}")

    # When the display doesn't contain any blanks, then you win the game
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # printing the stages
    print(needs.stages[lives])
