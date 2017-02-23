""" The lamest blackjack:
Only a dealer and a player. Dealer shows all cards. Dealer max hit is 17.
Only one of all aces at hand is 21, the rest are 1
"""
class Deck:
    """ Create a deck """
    def __init__(self):
        suite_set = [
            {'name': 'A', 'value': 1},
            {'name': '2', 'value': 2},
            {'name': '3', 'value': 3},
            {'name': '4', 'value': 4},
            {'name': '5', 'value': 5},
            {'name': '6', 'value': 6},
            {'name': '7', 'value': 7},
            {'name': '8', 'value': 8},
            {'name': '9', 'value': 9},
            {'name': '10', 'value': 10},
            {'name': 'J', 'value': 10},
            {'name': 'Q', 'value': 10},
            {'name': 'K', 'value': 10},
            ]
        suites = ['S', 'H', 'D', 'C']

        self.deck=[]
        for card in suite_set:
            for suite in suites:
                self.deck.append({})
                self.deck[len(self.deck)-1]['suite'] = suite
                self.deck[len(self.deck)-1]['name'] = card['name']
                self.deck[len(self.deck)-1]['value'] = card['value']

    def shuffle(self):
        import random
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

    def len(self):
        return len(self.deck)


class Hand:
    """ Create a hand """
    def __init__(self):
        self.hand = []
        self.scores = 0
        self.stand = False
        self.aces = False

    def deal(self, card):
        self.hand.append(card)
        if card['name'] =='A' and not self.aces:
            self.aces = True
            self.scores += 10
            # first Ace counts as 11, all consequent ones count as 1
        self.scores += card['value']

class PlayerHand(Hand):
    """ Extend a Hand to add custom method for a player """
    def set_stand(self):
        if self.scores >= 21:
            self.stand = True
        elif self.stand:
            print('You chose to stand last time around...')
        else:
            answers = 'hHsS'
            s = input('Stand or Hit (S/H) ? ')
            while s not in answers:
                s = input('Which? (S/H) ')
            if (s in 'sS'):
                self.stand = True
            print('You chose to %s' % ('Stand' if self.stand else 'Hit'))

class DealerHand(Hand):
    """ Extend a Hand to add custom method for a dealer """
    def set_stand(self):
        self.stand = (self.scores > 17)
        print('Dealer %s...' % ('stands' if self.stand else 'hits'))

class Blackjack():
    """ The game """
    def __init__(self):
        pass

    def round_up(self):
        if self.player.scores == 21:
            if self.dealer.scores != self.player.scores:
                print('You hit Blackjack!!')
            else:
                print('Draw with 21!!')
        elif self.dealer.scores == 21:
            if self.dealer.scores != self.player.scores:
                print('Dealer hit Blackjack!!')
        elif self.dealer.scores == self.player.scores and self.dealer.scores < 21:
            print('Draw with %i' % (self.dealer.scores))
        elif self.dealer.scores == self.player.scores and self.dealer.scores > 21:
            print('Both busted with %i' % (self.dealer.scores))
        elif self.dealer.scores < 21 and (self.dealer.scores > self.player.scores or self.player.scores > 21):
            print('Dealer wins with %i against your %i' % (self.dealer.scores, self.player.scores))
        elif self.player.scores < 21 and (self.dealer.scores < self.player.scores or self.dealer.scores > 21):
            print('You win with %i against dealer''s %i' % (self.player.scores, self.dealer.scores))
        else:
            print('I have no clue (both busted, really) ...')

    def play_round(self):
        if not self.player.stand:
            self.player.deal(self.deck.deal())
        if not self.dealer.stand:
            self.dealer.deal(self.deck.deal())

        print('Your hand: %s' % str((self.player.hand)))
        print('Your total: %i' % (self.player.scores))

        print('Dealer''s hand: %s' % (str(self.dealer.hand)))
        print('Dealer''s total: %i' % (self.dealer.scores))

        self.player.set_stand()
        self.dealer.set_stand()

        if self.dealer.stand and self.player.stand:
            self.round_up()
        else:
            self.play_round()

    def start_game(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = PlayerHand()
        self.dealer = DealerHand()
        self.player.deal(self.deck.deal())
        self.dealer.deal(self.deck.deal())
        self.play_round()

    def play(self):
        play = True
        answers = 'YyNn'
        while play:
            self.start_game()
            s = input('Wanna play again? (Y/N) : ')
            while s not in answers:
                s = input('Which? (Y/N) : ')
            play = (s in 'Yy')

game = Blackjack()
game.play()