import random
import time
import json
import copy

#TODO: implement opponent being more likely to switch cards after a draw/loss
class Player:
    def __init__(self, name):
        self.hp = 5
        self.hand = []
        self.name = name

    # adds a card to the players hand, removes the card from the deck
    def addCard(self, card, gameDeck):
        self.hand.append(card)
        gameDeck.remove(card)

    def healCards(self, monsters):
        for i in range(len(self.hand)):
            for j in range(len(monsters)):
                if self.hand[i]['name'] == monsters[j]['name']:
                    self.hand[i]['hp'] = monsters[j]['hp']

    def removeCard(self, card, gameDeck):
        gameDeck.append(card)
        self.hand.remove(card)


def printTavern(gameDeck):
    #TODO implement amount of cards based on rounds
    tavern = []
    for i in range(0,3):
        tavern.append(random.choice(gameDeck))

    print("\n" * 15)
    print("Tavern cards:")
    for card in tavern:
        # if no ability
        if card['ability'] == '':
            print("[{0}]: [{1}, {2}], {3}".format(card['name'], card['hp'], card['str'], card['type'].upper()), end="")
        else:
            # if ability 
            if card['ability'] == 'taunt' or 'shield' or 'poison':
                print("[{0}]: [{1}, {2}], {3} with {4}".format(card['name'], card['hp'], card['str'], 
                card['type'].upper(), card['ability'].upper()), end="")
            elif card['ability'] == 'frenzy':
                print("[{0}]: [{1}, {2}], {3} with {4} (Buff teammates by {5} after surviving an attack)".format(card['name'], card['hp'], 
                card['str'], card['type'].upper(), card['ability'].upper(), card['ability-property-amount']), end="")

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


def draw(card, player, gameDeck):
    player.addCard(card, gameDeck)


# gives the player a specific card for testing purposes
def forceAssignUser(user, gameDeck):
    user.addCard(gameDeck[11], gameDeck)
    user.addCard(gameDeck[12], gameDeck)


def forceAssignOpponent(opponent, gameDeck):
    opponent.addCard(gameDeck[7], gameDeck)
    opponent.addCard(gameDeck[0], gameDeck)


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
    draw(random.choice(gameDeck), player, gameDeck)
    player.removeCard(card, gameDeck)
    print("Your new hand is...\n")
    for card in player.hand:
        print("[{}]".format(card['name']).center(15), end="")
    print()
    printHand(player)
    input("Press anything to continue.")

    # player.removeCard(card)

def opponentCardSwitch(player, gameDeck):
    # opponent never wants to have jerry
    for card in player.hand:
        if card['name'] == 'Jerry':
            draw(random.choice(gameDeck), player, gameDeck)
            player.removeCard(card, gameDeck)
            print("Opponent is switching cards...")
            time.sleep(2)
            return player
    for card in player.hand:
        if card['hp'] < 3:
            # opponent has 1 in 5 chance of switching out a card with less than 3 hp
            if random.randint(1, 5) == 1:
                draw(random.choice(gameDeck), player, gameDeck)
                player.removeCard(card, gameDeck)
                print("Opponent is switching cards...")
                time.sleep(2)
                return player
        elif card['str'] < 4:
            # opponent has a 1 in 3 chance of switching out card with less than 4 str
            if random.randint(1, 3) == 1:
                draw(random.choice(gameDeck), player, gameDeck)
                player.removeCard(card, gameDeck)
                print("Opponent is switching cards...")
                time.sleep(2)
                return player
    return player

        

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
    print("{0}, {1}".format(player.name, player.hand[monster]))
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
            if userMonAtk >= len(user.hand):
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

            if opponentMonAtk >= len(opponent.hand):
                opponentMonAtk = 0
            while checkDeckHealth(opponent) < 0:
                opponentMonAtk += 1
            randUserMon = random.randint(0, len(user.hand) - 1)
            # if the chosen enemy monster is already dead, find a different one to attack
            while opponent.hand[randUserMon]['hp'] <= 0:
                randUserMon = random.randint(0, len(user.hand) - 1)
            print("opponentmonattk", opponentMonAtk)
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

#TODO: implement choosing a card from the presented pool (tavern)
def main():
    # this variable is so i can switch between testing vs a real run
    testing = True
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
            draw(card, user, gameDeck)

            card = random.choice(gameDeck)
            draw(card, opponent, gameDeck)
    else:
        # force assigning cards to user and opponent to check interactions
        # forceAssignUser(user, gameDeck)
        # forceAssignOpponent(opponent, gameDeck)
        while user.hp != 0 and opponent.hp != 0:
            printTavern(gameDeck)
            printBoard(user, opponent)
            print("\nDo you want to keep your cards or switch cards? Keep = K, Switch = S")
            choice = input("> ".casefold())

            if choice == "s":
                cardSwitch(user, gameDeck)

            opponentCardSwitch(opponent, gameDeck)

            combat(user, opponent)
            user.healCards(monsters)
            opponent.healCards(monsters)

    if opponent.hp == 0:
        print("{0} loses! {1} is the winner!".format(opponent.name, user.name))
    else:
        print("{0} loses! {1} is the winner!".format(user.name, opponent.name))

    # start game
    while user.hp != 0 and opponent.hp != 0:
        printBoard(user, opponent)
        print("\nDo you want to keep your cards or switch cards? Keep = K, Switch = S")
        choice = input("> ".casefold())

        if choice == "s":
            cardSwitch(user, gameDeck)

        opponentCardSwitch(opponent, gameDeck)

        combat(user, opponent)
        user.healCards(monsters)
        opponent.healCards(monsters)

    if opponent.hp == 0:
        print("{0} loses! {1} is the winner!".format(opponent.name, user.name))
    else:
        print("{0} loses! {1} is the winner!".format(user.name, opponent.name))


if __name__ == "__main__":
    main()
