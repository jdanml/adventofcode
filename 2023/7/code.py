# Advent of code Year 2023 Day 7 solution
# Author = jdanml
# Date = December 2023

# Imports
from collections import Counter

fivekind, fourkind, fullhouse, threekind, twopair, onepair, highcard = (
    [],
    [],
    [],
    [],
    [],
    [],
    [],
)


def create_hand_dict(input_data):
    data_dict = {}
    lines = input_data.strip().split("\n")
    for line in lines:
        key, value = line.split()
        data_dict[key] = int(value)
    return data_dict


def determine_hand(hand):
    counts = Counter(hand)
    freqs = sorted(counts.values(), reverse=True)

    if freqs == [5]:
        fivekind.append(hand)
    elif freqs == [4, 1]:
        fourkind.append(hand)
    elif freqs == [3, 2]:
        fullhouse.append(hand)
    elif freqs == [3, 1, 1]:
        threekind.append(hand)
    elif freqs == [2, 2, 1]:
        twopair.append(hand)
    elif freqs == [2, 1, 1, 1]:
        onepair.append(hand)
    elif freqs == [1, 1, 1, 1, 1]:
        highcard.append(hand)
    else:
        return "Invalid Hand"

    return fivekind, fourkind, fullhouse, threekind, twopair, onepair, highcard


def sort_hands(hand):
    card_strength = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }
    return [card_strength[card] for card in hand]


input_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

    hands_dict = create_hand_dict(input)

    for hand, value in hands_dict.items():
        (
            fivekind,
            fourkind,
            fullhouse,
            threekind,
            twopair,
            onepair,
            highcard,
        ) = determine_hand(hand)

    fivekind.sort(key=sort_hands)
    fourkind.sort(key=sort_hands)
    fullhouse.sort(key=sort_hands)
    threekind.sort(key=sort_hands)
    twopair.sort(key=sort_hands)
    onepair.sort(key=sort_hands)
    highcard.sort(key=sort_hands)

    ordered_hands = (
        highcard + onepair + twopair + threekind + fullhouse + fourkind + fivekind
    )

    # print (ordered_hands)

    total = 0
    for hand, bid in hands_dict.items():
        rank = ordered_hands.index(hand) + 1
        total += rank * bid

print("Part One : " + str(total))

fivekind, fourkind, fullhouse, threekind, twopair, onepair, highcard = (
    [],
    [],
    [],
    [],
    [],
    [],
    [],
)


def determine_hand(hand):
    original_hand = hand
    best_freqs = []
    if "J" in hand:
        best_hand = hand
        best_hand_type = 0
        for card in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]:
            temp_hand = hand.replace("J", card)
            counts = Counter(temp_hand)
            freqs = sorted(counts.values(), reverse=True)
            hand_type = max(freqs)
            if hand_type > best_hand_type:
                best_hand = temp_hand
                best_hand_type = hand_type
                best_freqs = freqs
    else:
        counts = Counter(original_hand)
        freqs = sorted(counts.values(), reverse=True)

    if best_freqs:
        freqs = best_freqs

    if freqs == [5]:
        fivekind.append(original_hand)
    elif freqs == [4, 1]:
        fourkind.append(original_hand)
    elif freqs == [3, 2]:
        fullhouse.append(original_hand)
    elif freqs == [3, 1, 1]:
        threekind.append(original_hand)
    elif freqs == [2, 2, 1]:
        twopair.append(original_hand)
    elif freqs == [2, 1, 1, 1]:
        onepair.append(original_hand)
    elif freqs == [1, 1, 1, 1, 1]:
        highcard.append(original_hand)
    else:
        return "Invalid Hand"

    return fivekind, fourkind, fullhouse, threekind, twopair, onepair, highcard


def sort_hands(hand):
    card_strength = {
        "J": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "Q": 11,
        "K": 12,
        "A": 13,
    }
    return [card_strength[card] for card in hand]


with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

    hands_dict = create_hand_dict(input)

    for hand, value in hands_dict.items():
        (
            fivekind,
            fourkind,
            fullhouse,
            threekind,
            twopair,
            onepair,
            highcard,
        ) = determine_hand(hand)

    fivekind.sort(key=sort_hands)
    fourkind.sort(key=sort_hands)
    fullhouse.sort(key=sort_hands)
    threekind.sort(key=sort_hands)
    twopair.sort(key=sort_hands)
    onepair.sort(key=sort_hands)
    highcard.sort(key=sort_hands)

    ordered_hands = (
        highcard + onepair + twopair + threekind + fullhouse + fourkind + fivekind
    )

    # print (ordered_hands)

    total = 0
    for hand, bid in hands_dict.items():
        rank = ordered_hands.index(hand) + 1
        total += rank * bid

print("Part Two : " + str(total))
