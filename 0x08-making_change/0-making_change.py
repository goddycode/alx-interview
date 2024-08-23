#!/usr/bin/python3
"""
0-making_change.py module
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    min_coins = [0] + [total + 1] * total

    if total <= 0:
        return 0

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == total + 1:
        return -1
    return min_coins[total]
