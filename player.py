
class Player:
    VERSION = "c2h5oh ver1"

    def betRequest(self, game_state):
        bet = 0
        if len(game_state['community_cards']) == 0:
            if game_state['bet_index'] == 0:
                bet = game_state['small_blind']
            elif game_state['bet_index'] == 1:
                bet = game_state['small_blind'] * 2
            else:
                bet = game_state['current_buy_in']
                # bet = game_state['current_buy_in'] - game_state['players']['in_action']['bet']
        else:
            bet = game_state['current_buy_in']
            # bet = game_state['current_buy_in'] - game_state['players']['in_action']['bet']
        return bet

    def is_pair_in_hand(self, game_state):
        return game_state['players']['in_action']['hole_cards'][0]['rank'] == game_state['players']['in_action']['hole_cards'][1]['rank']

    def showdown(self, game_state):
        pass
