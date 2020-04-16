import random
import time


# contains HP of players
class Score:
    def __init__(self):
        self.user_hp = 5
        self.opponent_hp = 5


def main():
    # monster name, monster dictionary contains 1:HP and 2:STR
    play()
    score = Score()
    user_hp = score.user_hp
    opponent_hp = score.opponent_hp
    monsters = {'Jerry': {'HP': 1, 'STR': 1},
                'Volvath': {'HP': 2, 'STR': 1},
                'Rat Man': {'HP': 1, 'STR': 2},
                'Kularne': {'HP': 2, 'STR': 2},
                'Underoather': {'HP': 3, 'STR': 3},
                'Twinild': {'HP': 1, 'STR': 4},
                'Trappe': {'HP': 5, 'STR': 2},
                # 'God of Death': {'HP': 20, 'STR': 20}
                'Outlaster': {'HP': 10, 'STR': 1},
                'Griever': {'HP': 5, 'STR': 6},
                'Junilet': {'HP': 3, 'STR': 5},
                'Ov': {'HP': 1, 'STR': 6},
                'Aselone': {'HP': 12, 'STR': 3},
                'The Offraider': {'HP': 2, 'STR': 4},
                'Grort': {'HP': 2, 'STR': 2},
                'Pike': {'HP': 7, 'STR': 7},
                }
    rounds = 0
    while opponent_hp != 0 and user_hp != 0:
        user_hand = []
        opponent_hand = []
        # give two cards to player and opponent
        user_hand.append(card_selection(monsters))
        user_hand.append(card_selection(monsters))
        opponent_hand.append(card_selection(monsters))
        opponent_hand.append(card_selection(monsters))
        print_board(user_hand, monsters, user_hp, opponent_hp)
        print("\n")
        choice = input("Do you want to [p]lay your card or [c]hoose a different card? ")

        if choice == 'c':
            print("Changing cards.")
            user_hand = card_selection(monsters)
            print("Your new card is {0}, [{1}, {2}].".format(user_hand, monsters[user_hand]['HP'],
                                                             monsters[user_hand]['STR']))
            time.sleep(1)
            print("Playing round.")
            time.sleep(1)
        # opponent_hand = opponent_change(user_hand, opponent_hand, monsters)
        winner = play_card(user_hand, opponent_hand, monsters, user_hp, opponent_hp)

        if winner == "o":
            opponent_hp -= 1
        elif winner == "u":
            user_hp -= 1
        rounds += 1
    if opponent_hp == 0:
        print("You won.")
    else:
        print("You lost.")


# gives a random monster from the card pool
def card_selection(monsters):
    # monsters_list = ['Jerry','Volvath','Rat Man','Kularne','Underoather','Twinild','Trappe','God of Death']

    # previous_card = None
    # while True:
    #     card = random.choice(list(monsters_dict.keys()))
    #     print(previous_card)
    #     if card != previous_card:
    #         yield card
    #         previous_card = card
    return random.choice(list(monsters.keys()))


# determines if the opponent should change their card (cheater)
def opponent_change(user_hand, opponent_hand, monsters):
    for i in range(len(opponent_hand)):
        op_hold = opponent_hand[i]
        if op_hold == 'Jerry':
            print("Your opponent is changing cards...")
            time.sleep(2)
            opponent_hand[i] = random.choice(list(monsters.keys()))
        else:
            for j in range(len(opponent_hand)):
                us_hold = user_hand[j]
                if monsters[us_hold]['HP'] > (monsters[op_hold]['STR'] / 2):
                    rando = random.randint(1, 100)
                    if rando in range(1, 47):
                        print("Your opponent is changing cards...")
                        time.sleep(2)
                        return random.choice(list(monsters.keys()))
    return opponent_hand


# prints out the game board between rounds
def print_board(user_hand, monsters, user_hp, opponent_hp):
    print("\n\n\n\n\n\n\n\n")
    print("Opponent HP: {0}".format(opponent_hp).center(20))
    print("[] []".center(20))
    print("-" * 20)
    print()
    for i in range(len(user_hand)):
        print("[{0}]".format(user_hand[i]).center(10), end="")
    print()
    print("\t", end="")
    for i in range(len(user_hand)):
        hold = user_hand[i]
        print("[{0}, {1}]".format(monsters[hold]['HP'], monsters[hold]['STR']).center(5), end=" ")
    print()
    print("Your HP: {0}".format(user_hp).center(20))


# reveals the opponents cards before initiating battle
def play_card(user_hand, opponent_hand, monsters, user_hp, opponent_hp):
    print("\n\n\n\n\n\n\n\n")
    print("Opponent HP: {0}".format(opponent_hp).center(20))
    for i in range(len(opponent_hand)):
        print("[{0}]".format(opponent_hand[i]).center(10), end="")
    print()
    print("\t", end="")
    for i in range(len(opponent_hand)):
        op_hold = opponent_hand[i]
        print("[{0}, {1}]".format(monsters[op_hold]['HP'], monsters[op_hold]['STR']).center(5), end=" ")
    print()
    print("-" * 20)
    print()
    for i in range(len(user_hand)):
        print("[{0}]".format(user_hand[i]).center(10), end="")
    print()
    print("\t", end="")
    for i in range(len(user_hand)):
        us_hold = user_hand[i]
        print("[{0}, {1}]".format(monsters[us_hold]['HP'], monsters[us_hold]['STR']).center(5), end="")
    print()
    print("Your HP: {0}".format(user_hp).center(20))
    print('\n')
    input("Press anything to continue to battle.")
    return battle(user_hand, opponent_hand, monsters)


def battle_opponent_hand(user_hand, opponent_hand, monsters):
    for i in range(len(opponent_hand)):
        print("[{0}]".format(opponent_hand[i]).center(10), end="")
    print()
    print("\t", end="")
    for i in range(len(opponent_hand)):
        us_hold = user_hand[i]
        op_hold = opponent_hand[i]
        print(
            "[{0}, {1}]".format((monsters[op_hold]['HP'] - monsters[us_hold]['STR']), monsters[op_hold]['STR']).center(
                5), end=" ")


def battle_user_hand(user_hand, opponent_hand, monsters):
    for i in range(len(user_hand)):
        print("[{0}]".format(user_hand[i]).center(10), end="")
    print()
    print("\t", end="")
    # user monster hp
    for i in range(len(user_hand)):
        us_hold = user_hand[i]
        op_hold = opponent_hand[i]
        print(
            "[{0}, {1}]".format((monsters[us_hold]['HP'] - monsters[op_hold]['STR']), monsters[us_hold]['STR']).center(
                5), end="")


def battle(user_hand, opponent_hand, monsters):
    # opp monster names
    global winner
    op_1_alive = True
    op_2_alive = True
    us_1_alive = True
    us_2_alive = True
    opponent_monster_1 = monsters[opponent_hand[0]]['HP'] - monsters[user_hand[0]]['STR']
    opponent_monster_2 = monsters[opponent_hand[1]]['HP'] - monsters[user_hand[1]]['STR']
    user_monster_1 = monsters[user_hand[0]]['HP'] - monsters[opponent_hand[0]]['STR']
    user_monster_2 = monsters[user_hand[1]]['HP'] - monsters[opponent_hand[1]]['STR']
    if opponent_monster_1 <= 0:
        op_1_alive = False
    if opponent_monster_2 <= 0:
        op_2_alive = False
    if user_monster_1 <= 0:
        us_1_alive = False
    if user_monster_2 <= 0:
        us_2_alive = False
    # opp monster hp
    battle_opponent_hand(user_hand, opponent_hand, monsters)
    print()
    print("-" * 20)
    print()
    # user monster names
    battle_user_hand(user_hand, opponent_hand, monsters)

    # opponent_monster = monsters[opponent_hand]['HP'] - monsters[user_hand]['STR']
    # user_monster = monsters[user_hand]['HP'] - monsters[opponent_hand]['STR']
    print()
    # keeps the battle going if all monsters are still alive
    if opponent_monster_1 > 0 or opponent_monster_2 > 0:
        print("Opp has 1 or more monsters alive")
        if user_monster_1 > 0 or user_monster_2 > 0:
            print("User has 1 or more monsters alive")
            # need to fix this part and print new health on future rounds
            while (opponent_monster_1 > 0 and user_monster_1 > 0) or (opponent_monster_2 > 0 and user_monster_2 > 0):
                input("Monsters still alive. Press anything to continue.")
                opponent_monster_1 = opponent_monster_1 - monsters[user_hand[0]]['STR']
                opponent_monster_2 = opponent_monster_2 - monsters[user_hand[1]]['STR']
                user_monster_1 = user_monster_1 - monsters[opponent_hand[0]]['STR']
                user_monster_2 = user_monster_2 - monsters[opponent_hand[1]]['STR']
                print("\n\n\n\n\n\n\n\n")
                for i in range(len(opponent_hand)):
                    print("[{0}]".format(opponent_hand[i]).center(10), end="")
                print()
                print("\t", end="")
                # opp monster hp
                for i in range(len(opponent_hand)):
                    us_hold = user_hand[i]
                    op_hold = opponent_hand[i]
                    print("[{0}, {1}]".format((monsters[op_hold]['HP']-monsters[us_hold]['STR']), monsters[op_hold]['STR']).center(5), end=" ")
                print()
                print("-" * 20)
                print()
                # user monster names
                for i in range(len(user_hand)):
                    print("[{0}]".format(user_hand[i]).center(10), end="")
                print()
                print("\t", end="")
                # user monster hp
                for i in range(len(user_hand)):
                    us_hold = user_hand[i]
                    op_hold = opponent_hand[i]
                    print("[{0}, {1}]".format((monsters[us_hold]['HP'] - monsters[op_hold]['STR']),
                                              monsters[us_hold]['STR']).center(5), end="")
                print()
                if opponent_monster_1 <= 0:
                    op_1_alive = False
                if opponent_monster_2 <= 0:
                    op_2_alive = False
                if user_monster_1 <= 0:
                    us_1_alive = False
                if user_monster_2 <= 0:
                    us_2_alive = False
    if (op_1_alive is False and us_1_alive is False) and (op_2_alive is False and us_2_alive is False):
        print("Draw.")
        winner = 'd'
        input("Press anything to continue.")
    elif (op_1_alive is False and op_2_alive is False) and (us_1_alive is True or us_2_alive is True):
        print("You won. Opponent takes 1 damage.")
        winner = "o"
        input("Press anything to continue.")
    elif (op_1_alive is True or op_2_alive is True) and (us_1_alive is False and us_2_alive is False):
        print("You lost. You take one damage.")
        winner = "u"
        input("Press anything to continue.")
    return winner


def play():
    print("Welcome to NGC. If you would to play, type \"play\" or \"quit\" to quit.")
    choice = input("> ").lower().strip()
    while choice not in ['play', 'quit']:
        print("Didn't understand your input. Try again.")
        choice = input("> ").lower().strip()
    if choice == 'play':
        print("Do you want to hear the instructions? [Y/N]")
        choice = input("> ").lower().strip()
        if choice == 'y':
            print("Here are the basic rules:\n\n")
            time.sleep(1)
            print("You and your opponent each have 5 health. Your goal is to play a card you think will beat theirs. ")
            time.sleep(2)
            print("Each monsters has HP and STR. When they attack, they will deal damage to the opponent's monster\n"
                  "and take damage from them. Whoever still has health wins.\n"
                  "If both monsters die, it's a draw. If both live, it's a draw.")
            time.sleep(2)
            print("You get one card each round and can choose to draw a different card one time before playing.")
            print("Defeat your opponent to win.")
            time.sleep(5)
            input("Press anything to continue instructions.")
            print("\n\n\n\n\n\n\n")
            print("EXAMPLE".center(20))
            print()
            print("Opponent HP: 5".center(20))
            print("\t\t []\n")
            print("-" * 20)
            print()
            print("[Twinild]".center(20))
            print("[1, 4]".center(20))
            print(" ^HP ^STR".center(22))
            print("Your HP: 5".center(20))
            input("Press anything to continue to the game.")
    else:
        print("See ya.")
        exit()


main()
