
class Player:
    VERSION = "c2h5oh ver1"

    def betRequest(self, game_state):
        return game_state['current_buy_in']

    def showdown(self, game_state):
        pass

