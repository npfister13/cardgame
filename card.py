class Card:
    def __init__(self, card):
        self.name = card['name']
        self.hp = card['hp']
        self.str = card['str']
        self.type = card['type']
        self.amount = card['amount']
        self.ability = card['ability']
        self.abilityProperty = card['ability-property']
        self.abilityPropertyAmount = card['ability-property-amount']
    
    def printCardStats(self):
        print(self.name)
        print("HP:", self.hp)
        print("STR:", self.str)
        print("Type:", self.type.upper())
        if self.ability != "":
            print("Ability:", self.ability.upper())
            # maybe add in an ability description to each card or each ability?
            if self.abilityProperty != "":
                print("Ability properties:", self.abilityProperty.upper())
                print("Ability properties amount:", self.abilityPropertyAmount)
        print()