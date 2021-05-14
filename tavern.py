import random

class Tavern:
    def __init__(self):
        self.round = 1
        # sellables are the amount of cards that can be sold at once during the round
        self.sellables = 3
        self.tier = 1
        self.tavernCards = []

    def printTavern(self, gameDeck):
        self.tavernCards.clear()
        sellables = 3
        for i in range(0, sellables):
            rando = random.choice(gameDeck)
            while rando.amount == 0:
                rando = random.choice(gameDeck)
            rando.amount -= 1
            self.tavernCards.append(rando)

        print("\n" * 15)
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
            i += 1
            print()
        print()
        # return tavern
