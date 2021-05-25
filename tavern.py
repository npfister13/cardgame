import random

class Tavern:
    def __init__(self):
        self.round = 0
        # sellables are the amount of cards that can be sold at once during the round
        self.sellables = 3
        self.tier = 0
        self.tavernCards = []
        self.tavernCost = 0
        # {round number: card amount}
        self.tavernCardAmount = {0: 3, 1: 4, 2: 4, 3: 5, 4: 5, 5: 6}
        self.freezeCards = False

    def enableTavern(self, gameDeck):
        if self.freezeCards == False:
            self.tavernCards.clear()
            for i in range(0, self.tavernCardAmount[self.tier]):
                rando = random.choice(gameDeck)
                while rando.amount == 0:
                    rando = random.choice(gameDeck)
                rando.amount -= 1
                self.tavernCards.append(rando)
        elif self.freezeCards == True and len(self.tavernCards) < self.tavernCardAmount[self.tier]:
            print("oh shit yo its not mastchingsdhj")
            while len(self.tavernCards) < self.tavernCardAmount[self.tier]:
                print("Amount of cards currently in tavern:", len(self.tavernCards))
                print("Amount of cards there should currently be:", self.tavernCardAmount[self.tier])
                rando = random.choice(gameDeck)
                while rando.amount == 0:
                    rando = random.choice(gameDeck)
                rando.amount -= 1
                self.tavernCards.append(rando)
        print("\n" * 15)
        self.printTavern()
        # return tavern
    
    def printTavern(self):
        print("Tavern cards:")
        i = 0
        for card in self.tavernCards:
            # if no ability
            # if card.ability == '':
            # [choice num] [cardname]: [hp, str], TYPE
            print("[{0}] [{1}]: [{2}, {3}], {4}".format(i, card.name, card.hp, card.str, card.type.upper()),
                end="")
            # if ability 
            if card.ability == 'taunt' or card.ability == 'shield' or card.ability == 'poison':
                # [choice num] [cardname]: [hp, str], TYPE (with) ABILITY
                print(" with {}".format(card.ability.upper()), end="")
            elif card.ability == 'frenzy':
                print(" with {0} (Buff teammates by {1} after surviving an attack)".format(card.ability.upper(),
                                                                                        card.abilityPropertyAmount),
                    end="")
            # elif card.ability == 
            print()
            i += 1
        print()

    def adjustTavernCost(self):
        print(self.tavernCardAmount[self.tier])
        self.tier += 1
    
    def removeCardFromTavern(self, choice):
        self.tavernCards.pop(choice)

    
