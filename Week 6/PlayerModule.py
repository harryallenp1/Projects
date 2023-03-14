class Player:
    def __init__(self, name : str) -> None:
        self._playerName = name
        self._guessedNumber = -1

    def playGame(self):
        #guess a positive integer number between 1 and 25

        #generate a random number

        #ask the user to input a number between 1 and 25
        self._guessedNumber = int(input("Enter your guess : "))

        print(f'{self._playerName} guessed {self._guessedNumber}')

