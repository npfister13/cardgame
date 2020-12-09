import random
import time
import json


class Player:
    def __init__(self):
        self.__hp = 5
        self.__hand = []

    def addCard(self, card):
        self.__hand.append(card)

    def printHand(self):
        print(self.__hand)

    # def switchCard(self, card, gameDeck):
    #     gameDeck.append(card)
    #     self.__hand.remove(card)


def draw(card, player):
    player.addCard(card)


# def switch(card, player, gameDeck):
#     draw(random.choice(gameDeck), player)
#     player.switchCard(card, gameDeck)


def main():
    with open('monsters.json', 'r') as f:
        monsters = json.load(f)
        gameDeck = monsters
    cardsInUse = []
    user = Player()
    opponent = Player()
    for i in range(2):
        card = random.choice(gameDeck)
        draw(card, user)
        gameDeck.remove(card)

        card = random.choice(gameDeck)
        draw(card, opponent)
        gameDeck.remove(card)

    user.printHand()
    opponent.printHand()


main()
