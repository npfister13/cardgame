import copy

class Player:
    def __init__(self, name):
        self.hp = 5
        self.hand = []
        self.name = name

    # adds a card to the players hand, removes the card from the deck
    def addCard(self, card):
        card.amount -= 1
        card = copy.deepcopy(card)
        self.hand.append(card)
        print("card amount", card.amount)

    def healCards(self, monsters):
        for i in range(len(self.hand)):
            for j in range(len(monsters)):
                if self.hand[i].name == monsters[j]['name']:
                    self.hand[i].hp = monsters[j]['hp']

    def removeCard(self, card, gameDeck):
        gameDeck.append(card)
        self.hand.remove(card)
