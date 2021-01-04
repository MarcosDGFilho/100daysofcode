import random, itertools
# First initialize a Deck class variable
# then you can shuffle the deck with Deck.shuffle()
# then to work with it just assign it to a variable
# like so: gameDeck = Deck.cards() <- then that will generate
# a list of all the cards you'll be using

# To add a player simply create a new variable of Player class
# you must give it one attribute of type str (it's the player's name/id)

class Deck: 
    def __init__(self, decks=1): #Deck is the amount of deck standard decks you'll be using. If none is given then you'll use just 1
        self.cards = []
        self.decks = int(decks)
        self.build()
            
    def build(self):
        suits = ['♠', '♦', '♥', '♣']
        ranks  = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        fullDeck = list(itertools.product(ranks, suits)) * self.decks
        for card in fullDeck:
            self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

class Player: 
    def __init__(self, name, score=0, softScore=0):
        self.name = name
        self.hand = []
        self.score = score
        self.softScore = softScore

    def introduce(self):
        print(f"Hello I'm {self.name}")

    def draw(self, baralho):
        self.hand.append(baralho.pop())
        self.score = 0
        self.softScore = 0
        for card in self.hand:
        
            if card[0] == "A":
                self.score += 1
                self.softScore += 11
            elif card[0] == "J" or card[0] == "Q" or card[0] == "K":
                self.score += 10
                self.softScore += 10
            else:
                self.score += card[0]
                self.softScore += card[0]
        #return print(f'''{self.name} Scores:
        ##Score: {self.score} Soft-score: {self.softScore}''')      
    def check_score(self):
        return print(f'''
{self.name} current score:
Score: {self.score}
Soft-score: {self.softScore}\n
''')
    
def show_hand_ascii(hand):
    def rank_top(hand):
        for card in hand:
            if card[0] == 10:
                space = ''
            else:
                space = ' '
            print(f"│{card[0]} {space}      │", end = '')
        print('')
    def rank_bot(hand):
        for card in hand:
            if card[0] == 10:
                space = ''
            else:
                space = ' '
            print(f"│       {space}{card[0]}│", end = '')
        print('')
    def suit(hand):
        for card in hand:
            print(f"│    {card[1]}    │", end = '')
        print('')

    print("┌─────────┐"*len(hand))
    rank_top(hand)
    print("│         │"*len(hand))
    print("│         │"*len(hand))
    suit(hand)
    print("│         │"*len(hand))
    print("│         │"*len(hand))
    rank_bot(hand)
    print("└─────────┘"*len(hand))

