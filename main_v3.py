import random
import time
import json


class Player:
    def __init__(self):
        self.hp = 5
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    # def switchCard(self, card, gameDeck):
    #     gameDeck.append(card)
    #     self.__hand.remove(card)


def draw(card, player):
    player.addCard(card)


# gives the player a specific card for testing purposes
def forceAssignUser(user, gameDeck):
    user.addCard(gameDeck[0])
    user.addCard(gameDeck[1])


def forceAssignOpponent(opponent, gameDeck):
    opponent.addCard(gameDeck[2])
    opponent.addCard(gameDeck[3])


# def switch(card, player, gameDeck):
#     draw(random.choice(gameDeck), player)
#     player.switchCard(card, gameDeck)

def printHand(cards):
    for i in cards.hand:
        print("[{0}, {1}] ".format(i['hp'], i['str']).center(15), end="")
    print()


def printBoard(user, opponent):
    print("\n" * 15)
    print("Opponent hp: {}".format(opponent.hp).center(30))
    for card in opponent.hand:
        print("[{}]".format(card['name']).center(15), end="")
    print()
    printHand(opponent)
    print("-" * 30)
    print("Your hp: {}".format(user.hp).center(30))
    for card in user.hand:
        print("[{}]".format(card['name']).center(15), end="")
    print()
    printHand(user)


def determine_first():
    # return random.choice(["o", "u"])
    return "o"


def combat(user, opponent):
    printBoard(user, opponent)
    print("\nBattle start!")
    whose_turn = determine_first()

    # monsters attack left to right
    # used to determine which monster is currently attacking
    userMonAtk = 0
    opponentMonAtk = 0
    if whose_turn == "u":
        print("User goes first!")
        pass
    elif whose_turn == "o":
        print("Opponent goes first!")
        randUserMon = random.randint(0, len(user.hand) - 1)
        opMonster = opponent.hand[opponentMonAtk]
        usMonster = user.hand[randUserMon]
        # takes the user monster being attacked and reduces by opponent monster str
        usMonster['hp'] -= opMonster['str']
        # opponent monster attacking also loses hp based on str of monster it attacks
        opMonster['hp'] -= usMonster['str']
        printBoard(user, opponent)
        print("Opponent's {0} attacks your {1}!".format(opMonster['name'], usMonster['name']))
        #TODO: Where you left off: checking how the opponent monster attacks randomly. Need to figure out how to ignore dead monsters and continue a fight (or stop when necessary)


def main():
    # this variable is so i can switch between testing vs a real run
    testing = True

    with open('monsters.json', 'r') as f:
        monsters = json.load(f)
        gameDeck = monsters
    cardsInUse = []
    user = Player()
    opponent = Player()
    if not testing:
        for i in range(2):
            card = random.choice(gameDeck)
            draw(card, user)
            gameDeck.remove(card)

            card = random.choice(gameDeck)
            draw(card, opponent)
            gameDeck.remove(card)
    else:
        forceAssignUser(user, gameDeck)
        forceAssignOpponent(opponent, gameDeck)

    # start game
    print("start game")
    while user.hp != 0 and opponent.hp != 0:
        printBoard(user, opponent)
        print("\nDo you want to keep your cards or switch cards? Keep = K, Switch = S")
        choice = input("> ".casefold())
        # TODO: Implement card switching

        combat(user, opponent)
        break


if __name__ == "__main__":
    main()
