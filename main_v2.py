import random
import time
import json


def main():
    with open('monsters.json', 'r') as f:
        monsters_dict = json.load(f)
    score = Score()
    user_hp = score.user_hp
    opponent_hp = score.opponent_hp
    user_hand = []
    opponent_hand = []
    add_card(user_hand, opponent_hand, monsters_dict)
    add_card(user_hand, opponent_hand, monsters_dict)
    # print("Your hand: ")
    # print(len(user_hand))
    # for i in range(len(user_hand)):
    #     print(user_hand[i]['Name'])
    #     print("[{0}, {1}]".format(user_hand[i]['HP'], user_hand[i]['STR']))

    print_board(user_hand, opponent_hand, user_hp, opponent_hp)
    # TODO: figure out how to handle combat


# prints out the board, duh
def print_board(user_hand, opponent_hand, user_hp, opponent_hp):
    for i in range(15):
        print("")
    print("Opponent HP: {}".format(opponent_hp).center(30))
    for i in range(len(opponent_hand)):
        print("[{}]".format(opponent_hand[i]['Name']).center(15), end="")
    print()
    print_hand(opponent_hand)
    print()
    print("-"*30)
    print("Your HP: {}".format(user_hp).center(30))
    for i in range(len(user_hand)):
        print("[{}]".format(user_hand[i]['Name']).center(15), end="")
    print()
    print_hand(user_hand)


# prints the hand given to it
def print_hand(hand):
    for i in range(len(hand)):
        hp = hand[i]['HP']
        strength = hand[i]['STR']
        print("[{0}, {1}] ".format(hp, strength).center(15), end="")


# adds a card to both player's hand at the beginning of the round
def add_card(user_hand, opponent_hand, monsters_dict):
    user_hand.append(random.choice(monsters_dict))
    opponent_hand.append(random.choice(monsters_dict))
    print("User hand: ", user_hand)
    print("Opponent hand: ", opponent_hand)


# contains HP of players
class Score:
    def __init__(self):
        self.user_hp = 5
        self.opponent_hp = 5


main()
