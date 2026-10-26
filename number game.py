import random
playing = True
number = str(random.randint(0, 9))
print('I will generate a random number between 0 & 9, and you have to guess 1 digit at a time.''')
print('The game ends when you have one hero.')
while playing:
    guess = input("Give me your best guess:\n")
    if number == guess:
        print("You win the game! \nThe number was ", number)
        break
    else:
        print("Your guess isn't quite right. Try again!")
        
