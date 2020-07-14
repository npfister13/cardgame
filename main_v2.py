import random
import time
import json

with open('monsters.json', 'r') as f:
    monsters_dict = json.load(f)
    placeholder_dict = monsters_dict


# contains hp of players
def round_number():
    Score.round_count += 1


class Score:
    round_count = 0

    def __init__(self):
        self.user_hp = 5
        self.opponent_hp = 5


class Player:
    number_of_cards = 0
    cards_in_use = []

    # establishes a hand
    def __init__(self):
        self.hand = []

    # draws a card for the user or opponent
    def draw(self):
        drawn_card = random.choice(placeholder_dict)
        Player.cards_in_use.append(drawn_card)
        print("Current cards in use: {}".format(Player.cards_in_use))
        placeholder_dict.remove(drawn_card)
        self.hand.append(drawn_card)
        Player.number_of_cards += 1

    # remove a chosen card from the users hand
    def switch(self, card):
        for i in monsters_dict:
            if i['name'] == card['name']:
                print("placeholdering")
                placeholder_dict.append(monsters_dict[card])
        # monsters_dict.append(card)
        self.hand.remove(card)
        print(placeholder_dict)

    def heal_monsters(self, card):
        print(self.hand)
        for i in self.hand:
            if i['name'] == card[i]['name']:
                print("Removing and replacing card with itself")
                self.hand.remove(card)
                self.hand.append(monsters_dict[card])
        print(self.hand)


# TODO: check to see if cards are being re-added to monster dict when switching cards
def main():
    user = Player()
    opponent = Player()
    score = Score()
    user_hp = score.user_hp
    opponent_hp = score.opponent_hp
    user.draw()
    user.draw()
    opponent.draw()
    opponent.draw()
    while user_hp != 0 or opponent_hp != 0:
        print_board(user, opponent, user_hp, opponent_hp)
        print()
        print("Do you want to keep your cards or switch cards? Keep = K, Switch = S")
        choice = input("> ").casefold()
        if choice == "s":
            return_card = switch_card(user)
            user.switch(return_card)
            user.draw()
            print_board(user, opponent, user_hp, opponent_hp)

        # TODO: figure out how to handle combat
        combat(user, opponent, user_hp, opponent_hp)


def switch_card(user):
    print()
    print()
    print("Which card do you want to switch?")
    i = 0
    for card in user.hand:
        print("[{}]".format(card['name']).center(15), end="")
    print()
    for card in user.hand:
        print("[{}]".format(i).center(15), end="")
        i += 1
    print()
    while True:
        try:
            choose_card = int(input("> "))
            if choose_card >= i:
                print("too high")
            elif choose_card < 0:
                print("too low")
            else:
                break
        except ValueError:
            print("input a number")
    i = 0
    for card in user.hand:
        if choose_card == i:
            return card
        i += 1


def combat(user, opponent, user_hp, opponent_hp):
    print_board(user, opponent, user_hp, opponent_hp)
    print("\nBattle start!")
    whose_turn = None
    if whose_turn is None:
        whose_turn = determine_first()
    elif whose_turn == "u":
        whose_turn = "o"
    elif whose_turn == "o":
        whose_turn = "u"
    # monsters attack from left to right, so these will count up to the
    # last card in their hand
    op_monster_to_attack = 0
    us_monster_to_attack = 0
    if whose_turn == "o":
        print("Opponent goes first.")
        press_continue()
        monster_attacking(user, opponent, us_monster_to_attack,
                          op_monster_to_attack, whose_turn, user_hp, opponent_hp)
    else:
        print("You go first.")
        press_continue()
        monster_attacking(user, opponent, us_monster_to_attack,
                          op_monster_to_attack, whose_turn, user_hp, opponent_hp)
    press_continue()


def opponent_attacking(user, opponent, op_monster_to_attack, user_hp, opponent_hp):
    # chooses a random card to attack
    user_hand = int(Player.number_of_cards / 2)
    us_monster = random.randint(0, user_hand - 1)
    op_card = opponent.hand
    us_card = user.hand
    while True:
        # choose a different monster to attack if the one chosen is already dead
        if us_card[us_monster]['hp'] <= 0:
            us_monster = random.randint(0, user_hand - 1)
        else:
            break
    print("op monster to attack: {}".format(op_monster_to_attack))
    try:
        op_card[op_monster_to_attack]['hp'] = (op_card[op_monster_to_attack]['hp'] -
                                               us_card[us_monster]['str'])
    except IndexError:
        print("IndexError caught, op_monster_to_attack outside of index range. Changing to 0.")
        op_monster_to_attack = 0
        op_card[op_monster_to_attack]['hp'] = (op_card[op_monster_to_attack]['hp'] -
                                               us_card[us_monster]['str'])
    us_card[us_monster]['hp'] = (us_card[us_monster]['hp']) - op_card[op_monster_to_attack]['str']
    print_board(user, opponent, user_hp, opponent_hp)
    print()
    print("{0} attacks {1}!".format(op_card[op_monster_to_attack]['name'], us_card[us_monster]['name']))
    op_monster_to_attack += 1
    return user, opponent, op_monster_to_attack, us_card, op_card


def user_attacking(user, opponent, us_monster_to_attack, user_hp, opponent_hp):
    # chooses a random card to attack, players always have an equal amount of cards
    opponent_hand = int(Player.number_of_cards / 2)
    op_monster = random.randint(0, opponent_hand - 1)
    op_card = opponent.hand
    us_card = user.hand
    try:
        us_card[us_monster_to_attack]['hp'] = (us_card[us_monster_to_attack]['hp'] -
                                               op_card[op_monster]['str'])
    except IndexError:
        print("IndexError caught, us_monster_to_attack outside of index range. Changing to 0.")
        us_monster_to_attack = 0
        us_card[us_monster_to_attack]['hp'] = (us_card[us_monster_to_attack]['hp'] -
                                               op_card[op_monster]['str'])

    op_card[op_monster]['hp'] = (op_card[op_monster]['hp']) - us_card[us_monster_to_attack]['str']
    print_board(user, opponent, user_hp, opponent_hp)
    print()
    print("{0} attacks {1}!".format(us_card[us_monster_to_attack]['name'], op_card[op_monster]['name']))
    us_monster_to_attack += 1
    return user, opponent, us_monster_to_attack, us_card, op_card


# this handles calculations for when one monster attacks another
def monster_attacking(user, opponent, us_monster_to_attack, op_monster_to_attack, whose_turn, user_hp, opponent_hp):
    user_cards_left = (Player.number_of_cards / 2)
    opponent_cards_left = (Player.number_of_cards / 2)
    op_monsters_alive = True
    us_monsters_alive = True
    while op_monsters_alive and us_monsters_alive:
        print(whose_turn)
        if whose_turn == "o":
            print("Beginning opponents turn")
            user, opponent, op_monster_to_attack, us_card, op_card = opponent_attacking(user, opponent,
                                                                                        op_monster_to_attack, user_hp,
                                                                                        opponent_hp)
            print(op_monster_to_attack)
            for i in op_card:
                if i['hp'] > 0:
                    op_monsters_alive = True
                    break
                else:
                    op_monsters_alive = False
            if op_monsters_alive:
                for i in us_card:
                    if i['hp'] > 0:
                        us_monsters_alive = True
                        break
                    else:
                        us_monsters_alive = False
                whose_turn = "u"
                input("Monster alive. Continuing. Press anything.")

        else:
            print("Beginning users turn")
            print("Us monster to attack: {}".format(us_monster_to_attack))
            user, opponent, us_monster_to_attack, us_card, op_card = user_attacking(user, opponent,
                                                                                    us_monster_to_attack, user_hp,
                                                                                    opponent_hp)
            for i in us_card:
                if i['hp'] > 0:
                    us_monsters_alive = True
                    break
                else:
                    us_monsters_alive = False
            if us_monsters_alive:
                for i in op_card:
                    if i['hp'] > 0:
                        op_monsters_alive = True
                        break
                    else:
                        op_monsters_alive = False
                whose_turn = "o"
                input("Monster alive. Continuing. Press anything.")

    else:
        if not op_monsters_alive:
            print("Opponents monsters are dead. They lose 1 HP.")
            opponent_hp -= 1
        elif not us_monsters_alive:
            print("Users monsters are dead. They lose 1 HP.")
            user_hp -= 1
    user.heal_monsters(user)
    opponent.heal_monsters(opponent)
    return user, opponent, whose_turn, user_hp, opponent_hp


def determine_first():
    # return random.choice(["o", "u"])
    return "o"


# prints out the board, duh
# TODO: have it to where print_board will only print a monster if its hp is above 0
def print_board(user, opponent, user_hp, opponent_hp):
    for i in range(15):
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


def press_continue():
    input("\nPress anything to continue.")


main()
