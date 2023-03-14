from PlayerModule import Player
import random

class GuessingGame:
    def __init__(self) -> None:
        self._correctNumber = -1
        self._attempts = 5
        self._player1 = Player("Larry")
        self._player2 = Player("Curly")
        self._player3 = Player("Moe")

    def startGame(self):
        self._correctNumber = random.randint(1, 25)
        
        print(f'I have a random number between 1 and 25. ' +
              f'You have {self._attempts} attempts to guess it correctly')
        print(f'correct Number : {self._correctNumber}')

        winner = False

        for i in range(self._attempts):
            self._player1.playGame() 
            #self._player2.playGame() 
            #self._player3.playGame() 

            print(f'Number of attempts remaining : {self._attempts - (i + 1)}')

            #call checkWinner() function, get the boolean result 
            #save the returned boolean value to winner variable
            winner = self.checkWinner()

            if winner:
                print(f'Winner found. Correct number was {self._correctNumber}')
                break

        else: #for..else
            print("Game Over. No winner found.")

    def checkWinner(self) -> bool:
        winnerFound = False

        if self._player1._guessedNumber == self._correctNumber:
            print(f'{self._player1._playerName} has guessed correct number {self._correctNumber}')
            winnerFound = True

        return winnerFound