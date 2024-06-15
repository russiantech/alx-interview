#!/usr/bin/python3


""" Given a pile of coins of different values, 
determine the fewest number of coins needed to meet a given amount total. 
"""
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the dp array with inf, and set dp[0] to 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Update the dp array for each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still inf, return -1 (total cannot be met with given coins)
    return dp[total] if dp[total] != float('inf') else -1
