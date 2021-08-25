import random
secret = random.randint(0, 50)
guess = 0
tries = 0
print("Hello, let's play the number guessing game.")
print("I have a number from 0 to 50. Try to guess which one it is. I'll give you 6 tries.")
while guess != secret and tries < 6:
    guess = int(input("What's your guess?"))
    if guess < secret:
        print("Too low, go higher!")
        tries = tries+1
        print("You have", 6-tries, "tries left.")
    elif guess > secret:
        print("Too high, go lower!")
        tries = tries+1
        print("You have", 6-tries, "tries left.")
if guess == secret:
    print("You are correct!")
else:
    print("Sorry, you're out of guesses. Better luck next time!")
    print("The number was", secret)
