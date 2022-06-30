def main():
    from random import randint

    play =  1 
    score = 0

    # Define strings
    def winStr(): print(f"You chose {playerStr}, and I chose {opponentStr}. Congratulations! You won! (Score = {score})")
    def loseStr(): print(f"You chose {playerStr}, and I chose {opponentStr}. Unfortunately, you lost. (Score = {score})")
    def drawStr(): print(f"You chose {playerStr}, and I chose {opponentStr}. It was a draw. (Score = {score})")

    while play == 1:
        # Get user input & choose value
        player = input("Rock, Paper, or Scissors? (r/p/s)\n"); player = player.lower()
        opponentInt = randint(1,3)

        # Assigning player input to int value
        playerInt = []
        if player == 'r': playerStr, playerInt = 'Rock', 1
        elif player == 'p': playerStr, playerInt = 'Paper', 2
        elif player == 's': playerStr, playerInt = 'Scissors', 3

        # Assigning randint function input to str value
        if opponentInt == 1: opponentStr = 'Rock'
        elif opponentInt == 2: opponentStr = 'Paper'
        elif opponentInt == 3: opponentStr = 'Scissors'

        # Give result of game
        if playerInt == []: print('Unexpected value, please play again and check spellings.')
        elif playerInt == 1 and opponentInt == 3: score += 1; winStr()
        elif playerInt == 3 and opponentInt == 1: score -= 1; loseStr()
        elif playerInt > opponentInt: score += 1; winStr()
        elif playerInt < opponentInt: score -= 1; loseStr() 
        elif playerInt == opponentInt: drawStr()

        # Ask user if they would wish to play again
        play = 2
        while play == 2:
            playAgain = input("Would you like to play again? (y/n)  ")
            playAgain = playAgain.lower()
            if playAgain == 'y': play = 1
            elif playAgain == 'n': play = 0
            else:
                play = 2
                print("Unexpected value...")

    # Print score
    print(f"Your score was {score}.")

if __name__ == "__main__":
    main()