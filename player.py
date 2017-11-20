class Player:
    VERSION = "c2h5oh ver2"
  
    # first bet round without communnity cards
    def first_round(self, game_state):
        if game_state['bet_index'] == 0:
            bet = game_state['small_blind']
        elif game_state['bet_index'] == 1:
            bet = game_state['small_blind'] * 2
        else:
            # player_idx = game_state['in_action']
            # bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet']
            bet = game_state['current_buy_in']
        return bet

    # 3 community cards
    def second_round(self, game_state):
        # bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet']
        bet = game_state['current_buy_in']
        return bet

    # 4 community cards
    def third_round(self, game_state):
        # bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet']
        bet = game_state['current_buy_in']
        return bet

    # 5 community cards
    def fourth_round(self, game_state):
        # bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet']
        bet = game_state['current_buy_in']
        return bet

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

        # self.transform_hand(game_state)

        return bet

    def is_pair_in_hand(self, game_state):
        player_idx = game_state['in_action']
        return game_state['players'][player_idx]['hole_cards'][0]['rank'] == game_state['players'][player_idx]['hole_cards'][1]['rank']

    def transform_hand(self, game_state):
        modified_hand = []
        player_idx = game_state['in_action']

        for card in game_state['players'][player_idx]['hole_cards']:

            if card['suit'] == 'clubs':
                modified_suit = 'C'
            elif card['suit'] == 'spades':
                modified_suit = 'S'
            elif card['suit'] == 'hearts':
                modified_suit = 'H'
            elif card['suit'] == 'diamonds':
                modified_suit = 'D'

            if card['rank'] == '10':
                modified_rank = 'T'
            else:
                modified_rank = card['rank']

            modified_hand.append(modified_suit + modified_rank)
        
        return modified_hand

    def showdown(self, game_state):
        pass
