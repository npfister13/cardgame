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
    #     print(user_hand[i]['name'])
    #     print("[{0}, {1}]".format(user_hand[i]['hp'], user_hand[i]['str']))

    print_board(user_hand, opponent_hand, user_hp, opponent_hp)
    input("\nPress anything to continue.")
    # TODO: figure out how to handle combat
    combat(user_hand, opponent_hand, user_hp, opponent_hp)


def combat(user_hand, opponent_hand, user_hp, opponent_hp):
    print_board(user_hand, opponent_hand, user_hp, opponent_hp)
    print("\n\tBattle start!")
    whose_turn = determine_first()
    # monsters attack from left to right, so these will count up to the
    # last card in their hand
    op_monster_to_attack = 0
    us_monster_to_attack = 0
    if whose_turn == "o":
        print("\tOpponent goes first.")
        monster_attacking(user_hand, opponent_hand, us_monster_to_attack,
                          op_monster_to_attack, whose_turn)
    else:
        print("\tYou go first.")


# this handles calculations for when one monster attacks another
def monster_attacking(user_hand, opponent_hand, us_monster_to_attack,
                      op_monster_to_attack, whose_turn):
    if whose_turn == "o":
        # grabs the monster from the opponents hand
        op_monster = opponent_hand[op_monster_to_attack]
        # chooses a random card to attack
        us_monster = user_hand[random.randint(0, len(user_hand))]
        # opponent_hand[op_monster['name']]['hp'] = (opponent_hand[op_monster]['hp'] - us_monster['str'])
        # user_hand[us_monster['name']]['hp'] = (user_hand[us_monster['hp']]) - op_monster['str']
        print("{0} attacks {1}!".format(op_monster['name'], us_monster['name']))


def determine_first():
    # return random.choice(["o", "u"])
    # TODO: change this back once opponent and user are finished
    return "o"


# prints out the board, duh
def print_board(user_hand, opponent_hand, user_hp, opponent_hp):
    for i in range(15):
        print("")
    print("Opponent hp: {}".format(opponent_hp).center(30))
    for i in range(len(opponent_hand)):
        print("[{}]".format(opponent_hand[i]['name']).center(15), end="")
    print()
    print_hand(opponent_hand)
    print()
    print("-"*30)
    print("Your hp: {}".format(user_hp).center(30))
    for i in range(len(user_hand)):
        print("[{}]".format(user_hand[i]['name']).center(15), end="")
    print()
    print_hand(user_hand)


# prints the hand given to it
def print_hand(hand):
    for i in range(len(hand)):
        hp = hand[i]['hp']
        strength = hand[i]['str']
        print("[{0}, {1}] ".format(hp, strength).center(15), end="")


# adds a card to both player's hand at the beginning of the round
def add_card(user_hand, opponent_hand, monsters_dict):
    user_hand.append(random.choice(monsters_dict))
    opponent_hand.append(random.choice(monsters_dict))
    print("User hand: ", user_hand)
    print("Opponent hand: ", opponent_hand)


# contains hp of players
class Score:
    def __init__(self):
        self.user_hp = 5
        self.opponent_hp = 5


main()
