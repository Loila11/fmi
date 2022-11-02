# Simularea unui joc de Toci
import random
import copy


def set_deck():
    # A -> 1, 2 -> 2, ..., 10 -> 10, J -> 11, Q -> 12, K -> 13
    deck = []
    for i in range(1, 14):
        deck.extend([(i, "clubs"), (i, "diamonds"), (i, "hearts"), (i, "spades")])

    return deck


def play_turn(no_players, stacks, center, player):
    card = stacks[player].pop()

    if card[0] == center[-1][0] + 1 or (card[0] == 1 and center[-1][0] == 13):
        center.append(card)
        return True

    for player2 in range(no_players):
        if player != player2 and stacks[player2] and \
                (card[0] == stacks[player2][-1][0] + 1 or (card[0] == 1 and stacks[player2][-1][0] == 13)):
            stacks[player2].append(card)
            return True

    stacks[player].append(card)
    return False


def game_simulation(no_players=2):
    stacks = [[] for i in range(no_players)]
    backwardStacks = [[] for i in range(no_players)]
    center = [(0, "start")]
    deck = set_deck()

    while True:
        for player in range(no_players):
            player_turn = True
            while player_turn:
                player_turn = False

                if stacks[player]:
                    player_turn = play_turn(no_players, stacks, center, player)

                if not player_turn:
                    if deck:
                        card = random.choice(deck)
                        deck.remove(card)
                    elif backwardStacks[player]:
                        card = backwardStacks[player].pop(0)
                    elif stacks[player]:
                        backwardStacks[player] = copy.deepcopy(stacks[player])
                        stacks[player] = []
                        card = backwardStacks[player].pop(0)
                    else:
                        return 1 if player == 0 else 0
                    stacks[player].append(card)
                    player_turn = play_turn(no_players, stacks, center, player)


def monte_carlo(no_players=2, no_tries=1000):
    wins = 0
    for i in range(no_tries):
        wins += game_simulation(no_players)

    return wins / no_tries


def main():
    print("Probabilitatea ca primul jucator sa castige intr-un joc cu 2 jucatori: " + str(monte_carlo()))
    print("Probabilitatea ca primul jucator sa castige intr-un joc cu 3 jucatori: " + str(monte_carlo(3)))
    print("Probabilitatea ca primul jucator sa castige intr-un joc cu 5 jucatori: " + str(monte_carlo(5)))


if __name__ == '__main__':
    main()
