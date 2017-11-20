
class Player:
    VERSION = "c2h5oh ver1"
  
    # first bet round without communnity cards
    def first_round(self, game_state):
        if game_state['bet_index'] == 0:
            bet = game_state['small_blind']
        elif game_state['bet_index'] == 1:
            bet = game_state['small_blind'] * 2
        else:
            bet = game_state['current_buy_in'] - game_state['players']['in_action']['bet']
        return bet

    # 3 community cards
    def second_round(self, game_state):
        return game_state['current_buy_in'] - game_state['players']['in_action']['bet']

    # 4 community cards
    def third_round(self, game_state):
        return game_state['current_buy_in'] - game_state['players']['in_action']['bet']

    # 5 community cards
    def fourth_round(self, game_state):
        return game_state['current_buy_in'] - game_state['players']['in_action']['bet']
    
    def betRequest(self, game_state):
        bet = 0
        if len(game_state['community_cards']) == 0:
            bet = self.first_round(game_state)
        elif len(game_state['community_cards']) == 3:
            bet = self.second_round(game_state)
        elif len(game_state['community_cards']) == 4:
            bet = self.third_round(game_state)
        elif len(game_state['community_cards']) == 5:
            bet = self.fourth_round(game_state) 
        return bet

    def showdown(self, game_state):
        pass
