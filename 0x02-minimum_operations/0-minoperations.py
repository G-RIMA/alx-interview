#!/usr/bin/python3


"""
Calculates the minimum operations
"""


def minOperations(n):

    dp = [n > 1 for i in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = i
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[i//j] + j)
    return dp[n]
