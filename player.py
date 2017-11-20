
import re


class Player:
    VERSION = "c2h5oh ver2"

    # first bet round without communnity cards
    def first_round(self, game_state):
        if game_state['bet_index'] == 0:
            bet = game_state['small_blind']
            # print 'BET_INDEX_0:' + str(bet)
        elif game_state['bet_index'] == 1:
            bet = game_state['small_blind'] * 2
            # print 'BET_INDEX_1:' + str(bet)
        else:
            cards = self.transform_hand(game_state)
            card1 = cards[0]
            card2 = cards[1]
            player_idx = game_state['in_action']

            if self.is_pair_in_hand(game_state):
                # bet = game_state['current_buy_in']
                if re.search('[AKQ]', card1):
                    bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet'] + game_state['minimum_raise'] * 2
                    # print 'BET_PAIR_AKQ:' + str(bet)
                elif re.search('[JT9]', card1):
                    bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet'] + game_state['minimum_raise']
                    # print 'BET_PAIR_JT9:' + str(bet)
                elif re.search('[2-8]', card1):
                    bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet']
                    # print 'BET_PAIR_2-8:' + str(bet)
                else:
                    bet = 0
            else:
                if re.search('[AKQ]', card1) and re.search('[AKQ]', card2):
                    bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet'] + game_state['minimum_raise'] * 2
                    # print 'BET_NOTPAIR_AKQ:' + str(bet)
                elif (re.search('[A]', card1) and re.search('[KQJT]', card2)) or (re.search('[KQJT]', card1) and re.search('[A]', card2)):
                    bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet']
                    # print 'BET_NOTPAIR_AKQ:' + str(bet)
                else:
                    bet = 0
                    # print 'BET_ELSE:' + str(bet)
            # player_idx = game_state['in_action']
            # bet = game_state['current_buy_in'] - game_state['players'][player_idx]['bet']
        # print 'FINAL_BET:' + str(bet)
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
