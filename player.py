import copy

class Player:
    def __init__(self, name):
        self.hp = 5
        self.hand = []
        self.name = name
        self.gold = 3
        self.goldMax = 10

    # adds a card to the players hand, removes the card from the deck
    def addCard(self, card):
        card.amount -= 1
        card = copy.deepcopy(card)
        self.hand.append(card)

    def healCards(self, monsters):
        for i in range(len(self.hand)):
            for j in range(len(monsters)):
                if self.hand[i].name == monsters[j]['name']:
                    self.hand[i].hp = monsters[j]['hp']

    def removeCard(self, card, gameDeck):
        gameDeck.append(card)
        self.hand.remove(card)
        print("Removing {0} and placing into deck.".format(card.name))

    def goldTotal(self):
        if self.gold != self.goldMax:
            self.gold += 1

    def addGold(self, amount):
        if self.gold != self.goldMax:
            self.gold += amount
    
    def setGold(self, rounds):
        self.gold = 3 + rounds
        if self.gold > 10:
            self.gold = 10
    
    def removeGold(self, amount):
        self.gold -= amount
