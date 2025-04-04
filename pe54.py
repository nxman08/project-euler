from collections import Counter

cv = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
      'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def get_rank(hand):
    values = sorted([cv[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]

    count = Counter(values)
    unique_counts = sorted(count.values(), reverse=True)

    flush = len(set(suits)) == 1
    straight = (values == list(range(values[0], values[0] - 5, -1)) or
                values == [14, 5, 4, 3, 2])

    if straight and flush:
        return (8, values)  # Straight Flush
    if unique_counts == [4, 1]:
        return (7, values)  # Four of a Kind
    if unique_counts == [3, 2]:
        return (6, values)  # Full House
    if flush:
        return (5, values)  # Flush
    if straight:
        return (4, values)  # Straight
    if unique_counts == [3, 1, 1]:
        return (3, values)  # Three of a Kind
    if unique_counts == [2, 2, 1]:
        return (2, values)  # Two Pair
    if unique_counts == [2, 1, 1, 1]:
        return (1, values)  # One Pair
    return (0, values)  # High Card

def winner(h1, h2):
    rank1, val1 = get_rank(h1)
    rank2, val2 = get_rank(h2)

    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return 2
    else:
        # Tie-breaker logic (corrected)
        counts1 = Counter([cv[c[0]] for c in h1])
        counts2 = Counter([cv[c[0]] for c in h2])

        vals1 = sorted(counts1.items(), key=lambda item: (item[1], item[0]), reverse=True)
        vals2 = sorted(counts2.items(), key=lambda item: (item[1], item[0]), reverse=True)

        for i in range(len(vals1)):
            if vals1[i][0] > vals2[i][0]:
                return 1
            elif vals2[i][0] > vals1[i][0]:
                return 2
        return 0  # Tie

with open("/Users/namanagarwal/VS code/project euler/0054_poker.txt", 'r') as f:
    rounds = [line.strip().split() for line in f]

# Count Player 1 wins
p1_wins = sum(1 for hand in rounds if winner(hand[:5], hand[5:]) == 1)

print(f"Player 1 wins: {p1_wins}")