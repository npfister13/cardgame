import random
import time
import json
import copy
# cannot resolve this issue below as it seems to be an on-going argument if it is a bug or feature with Pylance
import player
import card
import tavern

# TODO: implement opponent being more likely to switch cards after a draw/loss
# TODO: implement option select at beginning of rounds: Buy, Sell, End Turn



def chooseTavern(player, tavernCards, Tavern, gameDeck, Card):
    print("Choose the cards you would like. Each costs three (3) gold.\nEnd turn with E. Sell cards with S. Refresh tavern for one (1) gold with R.")
    print("Freeze cards for next turn with F.\nChange card order with C.")
    # theres gotta be a better way to do this
    inputList = ['E', 'S', 'C', 'R', 'F']
    while True:
        print("Gold total:", player.gold)
        while True:
            try:
                choice = input("> ")
                if int(choice) not in range(len(tavernCards)):
                    print("Selection out of range.")
                else:
                    break
            except ValueError:
                if choice not in inputList:
                    print("Please choose a valid option.")
                else:
                    break
        if choice.isnumeric() is True:
            if int(choice) in range(len(tavernCards)) and player.gold < 3: 
                print("You do not have enough gold.")
            else:
                index = tavernCards[int(choice)]
                player.addCard(index)
                player.gold -= 3
                Tavern.removeCardFromTavern(int(choice))
                Tavern.printTavern()
        if choice == 'E':
            print("Ending turn.")
            break
        elif choice == 'S':
            if player.hand == []:
                print("You have no cards to sell!")
            else:
                playerSellCard(player, tavernCards, Tavern, gameDeck, Card)
        elif choice == 'R':
            Tavern.enableTavern(gameDeck)
            player.removeGold(1)
        elif choice == 'F':
            Tavern.freezeCards = True
                

        
    

def checkPlayerInput(choice):
    if choice == 'E':
        pass

def playerSellCard(player, tavernCards, Tavern, gameDeck, Card):
    print("Which card would you like to sell?\n")
    for i in range(len(player.hand)):
        print("[{}]".format(i))
        Card.printCardStats(player.hand[i])
    while True:
        try:
            choice = int(input("> "))
            if choice not in range(len(tavernCards)):
                print("Selection out of range.")
            else:
                break
        except ValueError:
            print("Please input a number.")
    player.removeCard(player.hand[choice], gameDeck)
    player.addGold(1)

def draw(card, player, gameDeck):
    player.addCard(card)


# gives the player a specific card for testing purposes
def forceAssignUser(user, gameDeck):
    card = gameDeck[8]
    user.addCard(card)
    card = gameDeck[8]
    user.addCard(card)
    


def forceAssignOpponent(opponent, gameDeck):
    card = gameDeck[10]
    opponent.addCard(card)
    card = gameDeck[10]
    opponent.addCard(card)
    card = gameDeck[10]
    opponent.addCard(card)


def cardSwitch(player, gameDeck):
    print("Which card do you want to switch out?")
    for card in player.hand:
        print("[{}]".format(card.name).center(15), end="")
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
        print("[{}]".format(card.name).center(15), end="")
    print()
    printHand(player)
    input("Press anything to continue.")

    # player.removeCard(card)


def opponentCardSwitch(player, gameDeck):
    # opponent never wants to have jerry
    for card in player.hand:
        if card.name == 'Jerry':
            draw(random.choice(gameDeck), player, gameDeck)
            player.removeCard(card, gameDeck)
            print("Opponent is switching cards...")
            time.sleep(2)
            return player
    for card in player.hand:
        if card.hp < 3:
            # opponent has 1 in 5 chance of switching out a card with less than 3 hp
            if random.randint(1, 5) == 1:
                draw(random.choice(gameDeck), player, gameDeck)
                player.removeCard(card, gameDeck)
                print("Opponent is switching cards...")
                time.sleep(2)
                return player
        elif card.str < 4:
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
        print("[{0}, {1}] ".format(i.hp, i.str).center(15), end="")
    print()


def printBoard(user, opponent):
    print("\n" * 15)
    print("Opponent hp: {}".format(opponent.hp).center(30))
    for card in opponent.hand:
        print("[{}]".format(card.name).center(15), end="")
    print()
    printHand(opponent)
    print("-" * 30)
    print("Your hp: {}".format(user.hp).center(30))
    for card in user.hand:
        print("[{}]".format(card.name).center(15), end="")
    print()
    printHand(user)


def determineFirst():
    # first = "o"
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
        if player.hand[card].hp > 0:
            return True
    return False


def checkCardHealth(player, monster):
    # print("this is the monster:", monster)
    if monster >= len(player.hand):
        monster = 0
    #     print("monster value out of range, changing to 0")
    # print("{0}, {1}".format(player.name, player.hand[monster]))
    return player.hand[monster].hp


def checkAbility(attackingCard, receivingCard):
    if attackingCard.ability == 'shield':
        if receivingCard.ability == 'shield':
            # if they both have shield, damage is ignored for both
            print("both shield if statement")
            return attackingCard, receivingCard
        else:
            # if attacker has shield, only receivingCard takes damage
            print("only attacker has shield")
            receivingCard.hp -= attackingCard.str
            return attackingCard, receivingCard
    elif attackingCard.ability == 'poison':
        if receivingCard.ability == 'poison':
            # both cards insta die
            attackingCard.hp = 0
            receivingCard.hp = 0
            return attackingCard, receivingCard
        elif receivingCard.ability == 'shield':
            # receiving card lives due to shield, attacker takes damage
            attackingCard.hp -= receivingCard.str
            print("attacking card takes damage, receiver does not")
            return attackingCard, receivingCard
        else:
            # attacker takes damage, receiver insta dies
            attackingCard.hp -= receivingCard.str
            receivingCard.hp = 0
            print('else att/rec')
            return attackingCard, receivingCard
    elif receivingCard.ability == 'poison':
        receivingCard.hp -= attackingCard.str
        attackingCard.hp = 0
        return attackingCard, receivingCard
    receivingCard.hp -= attackingCard.str  # when attacking or being attacked, take damage
    attackingCard.hp -= receivingCard.str
    return attackingCard, receivingCard


# is it possible to refer to the winner/loser as opponent/user or vice versa without making print statements
# specifically for it?
# nvm, i guess i could make a .name for the self init
def combatEndMessage(winner, loser):
    print("{0} wins! {1} takes one damage.".format(winner.name, loser.name))
    loser.hp -= 1
    print("{0} now has {1} hp".format(loser.name, loser.hp))
    input("Press anything to continue.")


def interactionCalculation(attacker, receiver, attackerMonAtk, whoseTurn, attackerAlive, receiverAlive):
    while checkCardHealth(attacker, attackerMonAtk) <= 0:
        # use next monster if current is dead
        attackerMonAtk += 1
    if attackerMonAtk >= len(attacker.hand):
        # what monster will attack
        attackerMonAtk = 0
    # choose a random target
    try:
        randOpponentMon = random.randint(0, len(receiver.hand) - 1)
    except ValueError:
        # This error will come up if the receiver (likely the user) has no cards on the field
        receiverAlive = False
        return attacker, receiver, attackerMonAtk, attackerAlive, receiverAlive
        
    print(randOpponentMon)
    while receiver.hand[randOpponentMon].hp <= 0:
        # reroll if chosen enemy dead
        randOpponentMon = random.randint(0, len(receiver.hand) - 1)
        print(randOpponentMon)
    attackerMonster = attacker.hand[attackerMonAtk]  # store the card info
    receiverMonster = receiver.hand[randOpponentMon]
    # move damage calculations to checkAbility so that damage/hp modifiers can be done more easily
    attackerMonster, receiverMonster = checkAbility(attackerMonster, receiverMonster)
    if whoseTurn == "u":
        printBoard(attacker, receiver)
    else:
        printBoard(receiver, attacker)
    print("{0}'s {1} attacks {2}'s {3}!".format(attacker.name, attackerMonster.name, receiver.name,
                                                receiverMonster.name))
    receiverAlive = checkDeckHealth(receiver)
    attackerAlive = checkDeckHealth(attacker)
    input("Press anything to continue.")
    if attackerMonster.ability == 'windfury' and attackerMonster.hp > 0 and receiverAlive == True and attackerAlive == True:
        print("if windfury")
        for i in range(0, attackerMonster.abilityPropertyAmount):
            print("for loop")
            randOpponentMon = random.randint(0, len(attacker.hand) - 1)
            while receiver.hand[randOpponentMon].hp <= 0:
                # reroll if chosen enemy dead
                randOpponentMon = random.randint(0, len(attacker.hand) - 1)
            attackerMonster = attacker.hand[attackerMonAtk]  # store the card info
            receiverMonster = receiver.hand[randOpponentMon]
            # move damage calculations to checkAbility so that damage/hp modifiers can be done more easily
            attackerMonster, receiverMonster = checkAbility(attackerMonster, receiverMonster)
            if whoseTurn == "u":
                printBoard(attacker, receiver)
            else:
                printBoard(receiver, attacker)
            print("{0}'s {1} attacks {2}'s {3}!".format(attacker.name, attackerMonster.name, receiver.name,
                                                        receiverMonster.name))
            receiverAlive = checkDeckHealth(receiver)
            attackerAlive = checkDeckHealth(attacker)
            input("Press anything to continue.")
    attackerMonAtk += 1
    # print("{0} is alive = {1}".format(attacker.name, attackerAlive))
    # print("{0} is alive = {1}".format(receiver.name, receiverAlive))
    return attacker, receiver, attackerMonAtk, attackerAlive, receiverAlive


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
            print("")
            user, opponent, userMonAtk, userAlive, opponentAlive = interactionCalculation(user, opponent, userMonAtk,
                                                                                          whoseTurn, userAlive,
                                                                                          opponentAlive)
            whoseTurn = "o"

        elif whoseTurn == "o":
            print("")
            opponent, user, opponentMonAtk, opponentAlive, userAlive = interactionCalculation(opponent, user,
                                                                                              opponentMonAtk, whoseTurn,
                                                                                              opponentAlive, userAlive)
            whoseTurn = "u"

    if userAlive is False and opponentAlive is False:
        print("It's a draw!")
        input("Press anything to continue.\n")
    elif userAlive is False:
        combatEndMessage(opponent, user)
    else:
        combatEndMessage(user, opponent)
    print()


# TODO: implement choosing a card from the presented pool (tavern)
def main():
    # this variable is so i can switch between testing vs a real run
    testing = False
    Card = card.Card
    Player = player.Player
    Tavern = tavern.Tavern()

    with open('monsters.json', 'r') as f:
        monsters = json.load(f)
    gameDeck = []
    for i in range(len(monsters)):
        gameDeck.append(Card(monsters[i]))

    cardsInUse = []
    user = Player('User')
    opponent = Player('Opponent')
    if not testing:
        while user.hp != 0 and opponent.hp != 0:
            print(Tavern.round)
            Tavern.enableTavern(gameDeck)
            chooseTavern(user, Tavern.tavernCards, Tavern, gameDeck, Card)
            draw(random.choice(gameDeck), opponent, gameDeck)
            printBoard(user, opponent)
            input("Press anything to continue.")
            combat(user, opponent)
            user.healCards(monsters)
            opponent.healCards(monsters)
            Tavern.round += 1
            user.setGold(Tavern.round)

    else:
        # force assigning cards to user and opponent to check interactions
        forceAssignUser(user, gameDeck)
        forceAssignOpponent(opponent, gameDeck)
        
        while user.hp != 0 and opponent.hp != 0:
            # chooseTavern(user, tavern, gameDeck)
            # draw(random.choice(gameDeck), opponent, gameDeck)
            Tavern.enableTavern(gameDeck)
            chooseTavern(user, Tavern.tavernCards, Tavern, gameDeck, Card)
            printBoard(user, opponent)
            input("Press anything to continue.")
            combat(user, opponent)
            user.healCards(monsters)
            opponent.healCards(monsters)
            Tavern.round += 1
            Tavern.adjustTavernCost()

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
