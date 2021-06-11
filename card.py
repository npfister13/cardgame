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
    
    def __str__(self):

        #message = f"{self.name}\nHP: {self.hp}\nSTR: {self.str}\n"
        # message = f"{self.name}\n"
        # message += f"HP: {self.hp}"
        
        # messages = []
        # messages.append(self.name)
        # messages.append(f"HP: {self.hp}")
        # ...
        # return "\n".join(messages)

        messages = []
        messages.append(self.name)
        messages.append(f"HP: {self.hp}")
        messages.append(f"STR: {self.str}")
        messages.append(f"Type: {self.type.upper()}")

        if self.ability != "":
            messages.append(f"Ability: {self.ability.upper()}")
            # maybe add in an ability description to each card or each ability?
            if self.abilityProperty != "":
                messages.append(f"Ability properties: {self.abilityProperty.upper()}")
                messages.append(f"Ability properties amount: {self.abilityPropertyAmount}")

        return "\n".join(messages)
        
        # print(self.name)
        # print("HP:", self.hp)
        # print("STR:", self.str)
        # print("Type:", self.type.upper())
        # if self.ability != "":
        #     print("Ability:", self.ability.upper())
        #     # maybe add in an ability description to each card or each ability?
        #     if self.abilityProperty != "":
        #         print("Ability properties:", self.abilityProperty.upper())
        #         print("Ability properties amount:", self.abilityPropertyAmount)
        # print()