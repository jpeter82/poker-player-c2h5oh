
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        return game_state['small_blind'] * 2;

    def showdown(self, game_state):
        pass

