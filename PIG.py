import random

def roll(): #dice roll function
    minV = 1
    maxV = 6
    roll = random.randint(minV, maxV)

    return roll 

while True:
    players = input("How many people are playing? (min 2 - max 4) ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be 2 to 4 players")
    else:
        print("Invalid")

maxScore = 40
playerScores = [0 for _ in range(players)]

while max(playerScores) < maxScore:
    for playerIndex in range(players):
        print("\nPlayer", playerIndex + 1, "turn now\n")
        print("Your total score:", playerScores[playerIndex], "\n")
        currentScore = 0
        while True:
            shouldRoll = input("Would you like to roll? (*y* for yes) ")
            if shouldRoll.lower() != "y":
                break
            #else:
            value = roll()
            if value == 1:
                print("You rolled a 1 so your turn is done")
                currentScore = 0
                break
            else:
                currentScore += value
                print("You rolled a:", value)

            print("Your score is", currentScore)

        playerScores[playerIndex] += currentScore
        print("Your total score is:", playerScores[playerIndex])

maxScore = max(playerScores)
winIndex = playerScores.index(maxScore)
print("Player number", winIndex + 1, "has won with the score:", maxScore)


