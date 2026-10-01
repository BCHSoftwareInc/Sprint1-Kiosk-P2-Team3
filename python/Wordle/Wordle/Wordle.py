MAX_ATTEMPTS = 6
SECRET_WORD = "CRANE"
attempts_used = turn
print("======================================")
print(" WELCOME TO WORDLE! ")
print("Guess the 5-letter secret word.")
print("Feedback: [G] Green | [Y] Yellow | [_] Gray")
print("======================================")
guess = input("Attempt " + str(turn) + "/" + str(MAX_ATTEMPTS) + " - Enter a 5-letter word: ").upper()
for turn in range(1, MAX_ATTEMPTS + 1):

    valid_input = True
    print("Result:" + feedback)

    valid_input = False
    print("Invalid input! Please enter Exactly 5 letters. \n")



if guess == SECRET_WORD:
    won = True
    print("CONGRATULATIONS! You guessed it in " + str(attempts_used) + "attempts!")
else:
    print("GAME OVER! You ran out of attempts")
    print("The secret word was: " + SECRET_WORD)

