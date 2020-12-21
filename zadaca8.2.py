
secret = 11

guess = int(input("Guess the number (0-30)? "))

if secret == guess:
    print("Congratulations! You guessed the right number.")
else:
    print("Sorry, wrong number. Better luck next time!")