import random

playAgain = True

while playAgain:
    play = input("Would you like to play a dice game? (y/n): ")
    if play.lower() == "y":
        numDice = int(input("Let's roll the dice! How many dice would you like to roll? "))
        print("You chose " + str(numDice) + " dice")
        print("Rolling " + str(numDice) + " dice")
        total = 0
        for i in range(numDice):
            diceNumber = random.randint(1, 6)
            total += diceNumber
        print("You rolled a total of " + str(total))
        playAgain = input("Would you like to play again? (y/n): ").lower() == "y"
    else:
        break

print("Thanks for playing!")
