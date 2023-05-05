import os
import random
import time
import hangman_words
import hangman_art
from hangman_words import word_list

# Set up variables
difficulty = input("Choose difficulty level - easy, medium, or hard: ").lower()
if difficulty == "easy":
    chances = 7
    word_length = 4
    
elif difficulty == "medium":
    chances = 7
    word_length = 6
else:
    chances = 5
    word_length = 8

chosen_word = random.choice([word for word in word_list if len(word) == word_length])
game_continue = True
misses = []
s2 = ["_"] * word_length
score = {"win": 0, "lose": 0}

# Start game
print(hangman_art.logo)
print(" ".join(s2))

while(game_continue):
    guess_input = input("\nGuess: ").lower()
    guess = False
    os.system('clear')
        
    if guess_input in s2 or guess_input in misses:
        print(f"You have already guessed '{guess_input}'\n")
        
    else:
        for i in range(word_length):
            if guess_input == chosen_word[i]:
                guess = True
                s2[i] = chosen_word[i]
        
        if guess == False: #what happens when wrong choice is made
            print("You made a wrong guess.\n")
            chances -= 1
            misses.append(f"{guess_input}")
        else:
            print("Right guess.\n")
             # Check for a completed word after a correct guess
            if "_" not in s2:
                print(hangman_art.you_won)
                score["win"] += 1
                game_continue = False
                break  # End the while loop
        
    print(f'{" ".join(s2)}') #print the current updated string
    print("\nMisses: "+" ".join(misses)) 
    print(hangman_art.stages[chances])
        
    any_left = False
     
    if "_" in s2:
        any_left = True
        
    if any_left == False:
        print(hangman_art.you_won)
        score["win"] += 1
        game_continue = False    
        
    if chances == 0:
        game_continue = False
        score["lose"] += 1
        if any_left:
            print(hangman_art.game_over)
            print(f"Right answer was '{chosen_word}'")
    
    # Additional features
    if game_continue:
        print(f"Remaining time: {chances}s")
        if len(misses) > 0:
            print("Hint: ", random.choice([x for x in chosen_word if x not in s2]))
        print(f"Score - Wins: {score['win']}, Losses: {score['lose']}")
        
    if not any_left or chances == 0:
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again == "y":
            chosen_word = random.choice([word for word in word_list if len(word) == word_length])
           
