import random
import time
import json
import copy


class Player:
    def __init__(self, name):
        self.hp = 5
        self.hand = []
        self.name = name

    def addCard(self, card):
        self.hand.append(card)

    def healCards(self, monsters):
        for i in range(len(self.hand)):
            for j in range(len(monsters)):
                if self.hand[i]['name'] == monsters[j]['name']:
                    self.hand[i]['hp'] = monsters[j]['hp']

    def removeCard(self, card, gameDeck):
        gameDeck.append(card)
        self.hand.remove(card)


def draw(card, player):
    player.addCard(card)


# gives the player a specific card for testing purposes
def forceAssignUser(user, gameDeck):
    user.addCard(gameDeck[0])
    user.addCard(gameDeck[1])


def forceAssignOpponent(opponent, gameDeck):
    opponent.addCard(gameDeck[2])
    opponent.addCard(gameDeck[3])


def cardSwitch(player, gameDeck):
    print("Which card do you want to switch out?")
    for card in player.hand:
        print("[{}]".format(card['name']).center(15), end="")
    print()
    for i in range(len(player.hand)):
        print("[{}]".format(i).center(15), end="")
    print()
    while True:
        try:
            choice = int(input("> "))
            if choice not in range(len(player.hand)):
                print("Selection out of range. Which card do you want to switch out?")
            else:
                break
        except ValueError:
            print("Please input a number.")

    card = player.hand[choice]
    draw(random.choice(gameDeck), player)
    player.removeCard(card, gameDeck)
    print("Your new hand is...\n")
    for card in player.hand:
        print("[{}]".format(card['name']).center(15), end="")
    print()
    printHand(player)
    input("Press anything to continue.")

    # player.removeCard(card)


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


def determineFirst():
    first = "o"
    # return random.choice(["o", "u"])
    if first == "o":
        print("Opponent goes first!")
        return "o"
    else:
        print("User goes first!")
        return "u"


# this runs to check the HP of all monsters in the player's hand to determine if to continue fighting or not
def checkDeckHealth(player):
    for card in range(len(player.hand)):
        if player.hand[card]['hp'] > 0:
            return True
    return False


def checkCardHealth(player, monster):
    return player.hand[monster]['hp']


# is it possible to refer to the winner/loser as opponent/user or vice versa without making print statements
# specifically for it?
# nvm, i guess i could make a .name for the self init
def combatEndMessage(winner, loser):
    print("{0} wins! {1} takes one damage.".format(winner.name, loser.name))
    loser.hp -= 1
    print("{0} now has {1} hp".format(loser.name, loser.hp))
    input("Press anything to continue.")


def combat(user, opponent):
    printBoard(user, opponent)
    print("\nBattle start!")
    whoseTurn = determineFirst()
    userAlive = True
    opponentAlive = True
    # monsters attack left to right
    # used to determine which monster is currently attacking
    userMonAtk = 0
    opponentMonAtk = 0
    input("Press anything to continue.")
    while userAlive is not False and opponentAlive is not False:
        # TODO: turn the whole if/else statements into a function (or two) to reduce duplicate code
        if whoseTurn == "u":
            if userMonAtk > len(opponent.hand):
                userMonAtk = 0
            while checkCardHealth(user, userMonAtk) <= 0:
                userMonAtk += 1
            randOpponentMon = random.randint(0, len(user.hand) - 1)
            while opponent.hand[randOpponentMon]['hp'] <= 0:
                randOpponentMon = random.randint(0, len(user.hand) - 1)
            usMonster = user.hand[userMonAtk]
            opMonster = opponent.hand[randOpponentMon]
            opMonster['hp'] -= usMonster['str']
            usMonster['hp'] -= opMonster['str']
            printBoard(user, opponent)
            print("Your {0} attacks opponent's {1}!".format(usMonster['name'], opMonster['name']))
            opponentAlive = checkDeckHealth(opponent)
            userAlive = checkDeckHealth(user)
            input("Press anything to continue.")
            whoseTurn = "o"
            userMonAtk += 1

        elif whoseTurn == "o":

            while checkDeckHealth(opponent) < 0:
                opponentMonAtk += 1
            if opponentMonAtk > len(opponent.hand):
                opponentMonAtk = 0
            randUserMon = random.randint(0, len(user.hand) - 1)
            # if the chosen enemy monster is already dead, find a different one to attack
            while opponent.hand[randUserMon]['hp'] <= 0:
                randUserMon = random.randint(0, len(user.hand) - 1)
            opMonster = opponent.hand[opponentMonAtk]
            usMonster = user.hand[randUserMon]
            # takes the user monster being attacked and reduces by opponent monster str
            usMonster['hp'] -= opMonster['str']
            # opponent monster attacking also loses hp based on str of monster it attacks
            opMonster['hp'] -= usMonster['str']
            printBoard(user, opponent)
            print("Opponent's {0} attacks your {1}!".format(opMonster['name'], usMonster['name']))
            userAlive = checkDeckHealth(user)
            opponentAlive = checkDeckHealth(opponent)
            input("Press anything to continue.")
            whoseTurn = "u"
            opponentMonAtk += 1
    if userAlive is False and opponentAlive is False:
        print("It's a draw!")
        input("Press anything to continue.\n")
    elif userAlive is False:
        combatEndMessage(opponent, user)
    else:
        combatEndMessage(user, opponent)
    print()


def main():
    # this variable is so i can switch between testing vs a real run
    testing = False
    gameDeck = []
    with open('monsters.json', 'r') as f:
        monsters = json.load(f)
    gameDeck = copy.deepcopy(monsters)
    cardsInUse = []
    user = Player('User')
    opponent = Player('Opponent')
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
    while user.hp != 0 and opponent.hp != 0:
        printBoard(user, opponent)
        print("\nDo you want to keep your cards or switch cards? Keep = K, Switch = S")
        choice = input("> ".casefold())
        # TODO: Implement card switching

        if choice == "s":
            cardSwitch(user, gameDeck)

        combat(user, opponent)
        user.healCards(monsters)
        opponent.healCards(monsters)

        # TODO: Refill the health of cards at the end of a turn
    if opponent.hp == 0:
        print("{0} loses! {1} is the winner!".format(opponent.name, user.name))
    else:
        print("{0} loses! {1} is the winner!".format(user.name, opponent.name))


if __name__ == "__main__":
    main()
