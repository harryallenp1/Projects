from GameModule import GuessingGame

class Application:
    def runApp(self):
        game = GuessingGame()
        game.startGame()

app = Application()
app.runApp()
