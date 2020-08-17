"""
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from collections import Counter
from operator import itemgetter
hands = (line.split() for line in open("poker.txt"))

values = {r: i for i, r in enumerate('23456789TJQKA', 2)}
straights = [14, 5, 4, 3, 2] # Straight with an Ace; 14 handled later
for i in range(14, 5, -1):
    straights.append([i, i-1, i-2, i-3, i-4])
hierarchy = [[1,1,1,1,1], [2,1,1,1], [2,2,1], [3,1,1], [], [], [3,2], [4,1]] #empty = straight and flush

def evaluate_hand(hand1, hand2):
    hands = [hand1, hand2]
    total = []
    player_highs = []
    for hand in hands:
        card_count = Counter(card[0] for card in hand)
        card_values = []
        hand_type = []
        weighted_values = []
        for k, v in card_count.items():
            val = values[k]
            weighted_values.append([v, val])
            weighted_values.sort(key=itemgetter(0, 1), reverse=True) # Multiples of a card are worth more than a high card
            hand_type.append(v)
        for card in weighted_values:
            card_values.append(card[1])
        hand_type.sort(reverse=True)
        score = hierarchy.index(hand_type)
        if score == 0: # No matching card values; possible straight or flush
            if card_values in straights: # Checks for a straight
                score = 4
                if card_values[4] == 2:
                    card_values[0] = 1 # Changes to a low Ace
                    card_values.sort(reverse=True)
            if len(set(card[1] for card in hand)) == 1: # Checks for a flush
                if score == 4:
                    score = 8 # Straight flush
                else:
                    score = 5
        total.append(score)
        player_highs.append(card_values)

    if total[0] > total[1]: # Player 1 wins
        return 1
    if total[0] == total[1]:
        for card in range(len(player_highs[0])): # Compares high cards
            if player_highs[0][card] > player_highs[1][card]:
                return 1
            if player_highs[0][card] < player_highs[1][card]:
                return 0
        return None # This is a tie
    return 0 # PLayer2 wins

# [:5] is Player 1; [5:] is Player 2
print(sum(evaluate_hand(hand[:5], hand[5:]) for hand in hands))
