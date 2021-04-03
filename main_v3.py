import random
import time
import json
import copy

#TODO: implement opponent being more likely to switch cards after a draw/loss
#TODO: implement option select at beginning of round: Buy, Sell, End Turn
class Player:
    def __init__(self, name):
        self.hp = 5
        self.hand = []
        self.name = name

    # adds a card to the players hand, removes the card from the deck
    def addCard(self, card, gameDeck):
        card['amount'] -= 1
        card = copy.deepcopy(card)
        self.hand.append(card)
        # gameDeck.remove(card)
        print("card amount", card['amount'])


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
        rando = random.choice(gameDeck)
        while rando['amount'] == 0:
            rando = random.choice(gameDeck)
        rando['amount'] -= 1
        tavern.append(rando)

    print("\n" * 15)
    print("Tavern cards:")
    i = 0
    for card in tavern:
        # if no ability
        # if card['ability'] == '':
        # [choice num] [cardname]: [hp, str], TYPE
        print("[{0}] [{1}]: [{2}, {3}], {4}".format(i, card['name'], card['hp'], card['str'], card['type'].upper()), end="")
        # if ability 
        if card['ability'] == 'taunt' or card['ability'] == 'shield' or card['ability'] == 'poison':
            # [choice num] [cardname]: [hp, str], TYPE (with) ABILITY
            print(" with {}".format(card['ability'].upper()), end="")
        elif card['ability'] == 'frenzy':
            print(" with {0} (Buff teammates by {1} after surviving an attack)".format(card['ability'].upper(), card['ability-property-amount']), end="")
        # elif card['ability'] == 
        i+=1
        print()
    print()
    return tavern

def chooseTavern(player, tavern, gameDeck):
    print("Which card would you like? Pick one.")
    while True:
        try:
            choice = int(input("> "))
            if choice not in range(len(tavern)):
                print("Selection out of range. Which card do you want?")
            else:
                break
        except ValueError:
            print("Please input a number.")
    index = tavern[choice]
    player.addCard(index, gameDeck)
    

def draw(card, player, gameDeck):
    player.addCard(card, gameDeck)


# gives the player a specific card for testing purposes
def forceAssignUser(user, gameDeck):
    card = gameDeck[7]
    user.addCard(card, gameDeck)
    card = gameDeck[5]
    user.addCard(card, gameDeck)
    

def forceAssignOpponent(opponent, gameDeck):
    card = gameDeck[8]
    opponent.addCard(card, gameDeck)
    card = gameDeck[14]
    opponent.addCard(card, gameDeck)


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
    # first = "u"
    first = random.choice(["o", "u"])
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
    # print("this is the monster:", monster)
    if monster >= len(player.hand):
        monster = 0
    #     print("monster value out of range, changing to 0")
    # print("{0}, {1}".format(player.name, player.hand[monster]))
    return player.hand[monster]['hp']

def checkAbility(attackingCard, receivingCard):
    if attackingCard['ability'] == 'shield':
        if receivingCard['ability'] == 'shield':
            #if they both have shield, damage is ignored for both
            return attackingCard, receivingCard
        else:
            #if attacker has shield, only receivingCard takes damage
            receivingCard['hp'] -= attackingCard['str']
    elif attackingCard['ability'] == 'poison':
        if receivingCard['ability'] == 'poison':
            #both cards insta die
            attackingCard['hp'] = 0
            receivingCard['hp'] = 0
            return attackingCard, receivingCard
        elif receivingCard['ability'] == 'shield':
            # receiving card lives due to shield, attacker takes damage
            attackingCard['hp'] -= receivingCard['str']
            return attackingCard, receivingCard
        else:
            #attacker takes damage, receiver insta dies
            attackingCard['hp'] -= receivingCard['str']
            receivingCard['hp'] = 0
            return attackingCard, receivingCard
    receivingCard['hp'] -= attackingCard['str'] #when attacking or being attacked, take damage
    attackingCard['hp'] -= receivingCard['str']
    return attackingCard, receivingCard

    

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
        # TODO: add check to see if any opponent cards has taunt
        # TODO: add check to see if attacking card has windfury
        if whoseTurn == "u":
            while checkCardHealth(user, userMonAtk) <= 0:
                #use next monster if current is dead
                userMonAtk += 1
            if userMonAtk >= len(user.hand):
                #what monster will attack
                userMonAtk = 0
            #choose a random target
            randOpponentMon = random.randint(0, len(user.hand) - 1)
            while opponent.hand[randOpponentMon]['hp'] <= 0:
                #reroll if chosen enemy dead
                randOpponentMon = random.randint(0, len(user.hand) - 1)
            usMonster = user.hand[userMonAtk] #store the card info
            opMonster = opponent.hand[randOpponentMon]
            # move damage calculations to checkAbility so that damage/hp modifiers can be done more easily
            usMonster, opMonster = checkAbility(usMonster, opMonster)
            printBoard(user, opponent)
            print("Your {0} attacks opponent's {1}!".format(usMonster['name'], opMonster['name']))
            opponentAlive = checkDeckHealth(opponent)
            userAlive = checkDeckHealth(user)
            if usMonster['ability'] == 'windfury':
                randOpponentMon = random.randint(0, len(user.hand) - 1)

            input("Press anything to continue.")
            whoseTurn = "o"
            userMonAtk += 1

        elif whoseTurn == "o":

            while checkCardHealth(opponent, opponentMonAtk) <= 0:
                #use next monster if current is dead
                opponentMonAtk += 1
            if opponentMonAtk >= len(opponent.hand):
                opponentMonAtk = 0
            randUserMon = random.randint(0, len(user.hand) - 1)
            # if the chosen enemy monster is already dead, find a different one to attack
            while user.hand[randUserMon]['hp'] <= 0:
                randUserMon = random.randint(0, len(user.hand) - 1)
                print("opponent while loop for choosing target")
            # print("opponentmonattk", opponentMonAtk)
            opMonster = opponent.hand[opponentMonAtk]
            usMonster = user.hand[randUserMon]
            # move damage calculations to checkAbility so that damage/hp modifiers can be done more easily
            usMonster, opMonster = checkAbility(usMonster, opMonster)
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
    round = 1
    if not testing:
        while user.hp != 0 and opponent.hp != 0:
            tavern = printTavern(gameDeck)
            chooseTavern(user, tavern, gameDeck)
            draw(random.choice(gameDeck), opponent, gameDeck)
            printBoard(user, opponent)
            # if round > 1:
            #     print("\nDo you want to keep your cards or switch cards? Keep = K, Switch = S")
            #     choice = input("> ".casefold())

            #     if choice == "s":
            #         cardSwitch(user, gameDeck)
            #     opponentCardSwitch(opponent, gameDeck)
            input("Press anything to continue.")
            combat(user, opponent)
            user.healCards(monsters)
            opponent.healCards(monsters)
            round += 1
    else:
        # force assigning cards to user and opponent to check interactions
        forceAssignUser(user, gameDeck)
        forceAssignOpponent(opponent, gameDeck)
        while user.hp != 0 and opponent.hp != 0:
            tavern = printTavern(gameDeck)
            # chooseTavern(user, tavern, gameDeck)
            # draw(random.choice(gameDeck), opponent, gameDeck)
            printBoard(user, opponent)
            # if round > 1:
            #     print("\nDo you want to keep your cards or switch cards? Keep = K, Switch = S")
            #     choice = input("> ".casefold())

            #     if choice == "s":
            #         cardSwitch(user, gameDeck)
            #     opponentCardSwitch(opponent, gameDeck)
            input("Press anything to continue.")
            combat(user, opponent)
            user.healCards(monsters)
            opponent.healCards(monsters)
            round += 1

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
