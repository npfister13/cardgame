import random
import time
import json


with open('monsters.json', 'r') as f:
    monsters_dict = json.load(f)


# contains hp of players
class Score:
    def __init__(self):
        self.user_hp = 5
        self.opponent_hp = 5


class Player:

    # establishes a hand
    def __init__(self):
        self.hand = []

    # draws a card for the user or opponent
    def draw(self):
        drawn_card = random.choice(monsters_dict)
        monsters_dict.remove(drawn_card)
        self.hand.append(drawn_card)
        print(self.hand)

    # TODO: check this works
    def switch(self, card):
        monsters_dict.append(card)
        self.hand.remove(card)


def main():
    user = Player()
    opponent = Player()
    score = Score()
    user_hp = score.user_hp
    opponent_hp = score.opponent_hp
    user.draw()
    opponent.draw()
    print(user.hand)
    print(user.hand[0]['name'])
    for card in user.hand:
        print("[{}]".format(card['name']))
    # user_hand = []
    # opponent_hand = []
    # add_card(user, opponent, monsters_dict)
    # add_card(user, opponent, monsters_dict)
    # print("Your hand: ")
    # print(len(user_hand))
    # for i in range(len(user_hand)):
    #     print(user_hand[i]['name'])
    #     print("[{0}, {1}]".format(user_hand[i]['hp'], user_hand[i]['str']))

    print_board(user, opponent, user_hp, opponent_hp)
    input("\nPress anything to continue.")
    # TODO: figure out how to handle combat
    # combat(user_hand, opponent_hand, user_hp, opponent_hp)


def combat(user_hand, opponent_hand, user_hp, opponent_hp):
    print_board(user_hand, opponent_hand, user_hp, opponent_hp)
    print("\nBattle start!")
    whose_turn = determine_first()
    # monsters attack from left to right, so these will count up to the
    # last card in their hand
    op_monster_to_attack = 0
    us_monster_to_attack = 0
    if whose_turn == "o":
        print("Opponent goes first.")
        monster_attacking(user_hand, opponent_hand, us_monster_to_attack,
                          op_monster_to_attack, whose_turn, user_hp, opponent_hp)
    else:
        print("You go first.")


# this handles calculations for when one monster attacks another
def monster_attacking(user_hand, opponent_hand, us_monster_to_attack,
                      op_monster_to_attack, whose_turn, user_hp, opponent_hp):
    if whose_turn == "o":
        # chooses a random card to attack
        us_monster = random.randint(0, len(user_hand) - 1)
        opponent_hand[op_monster_to_attack]['hp'] = (opponent_hand[op_monster_to_attack]['hp'] -
                                                     user_hand[us_monster]['str'])
        user_hand[us_monster]['hp'] = (user_hand[us_monster]['hp']) - opponent_hand[op_monster_to_attack]['str']
        print_board(user_hand, opponent_hand, user_hp, opponent_hp)
        print()
        print("{0} attacks {1}!".format(opponent_hand[op_monster_to_attack]['name'], user_hand[us_monster]['name']))
        return user_hand, opponent_hand


def determine_first():
    # return random.choice(["o", "u"])
    # TODO: change this back once opponent and user are finished
    return "o"


# prints out the board, duh
# TODO: have it to where print_board will only print a monster if its hp is above 0
def print_board(user, opponent, user_hp, opponent_hp):
    for i in range(5):
        print("")
    print("Opponent hp: {}".format(opponent_hp).center(30))
    for card in opponent.hand:
        print("[{}]".format(card['name']).center(15), end="")
    print()
    print_hand(opponent)
    print()
    print("-" * 30)
    print("Your hp: {}".format(user_hp).center(30))
    for card in user.hand:
        print("[{}]".format(card['name']).center(15), end="")
    print()
    print_hand(user)


# prints the hand given to it
def print_hand(cards):
    for i in cards.hand:
        hp = i['hp']
        strength = i['str']
        print("[{0}, {1}] ".format(hp, strength).center(15), end="")

# adds a card to both player's hand at the beginning of the round
def add_card(user_hand, opponent_hand, monsters_dict):
    user_hand.append(random.choice(monsters_dict))
    opponent_hand.append(random.choice(monsters_dict))
    print("User hand: ", user_hand)
    print("Opponent hand: ", opponent_hand)


main()
