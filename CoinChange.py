import sys
class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        f = [sys.maxsize] * (amount+1)
        f[0] = 0
        for i in range(0, amount+1):
            for j in range(len(coins)):
                if i >= coins[j] and f[i-coins[j]] != sys.maxsize:
                       f[i] = min(f[i-coins[j]]+1, f[i])

        if f[amount] == sys.maxsize:
            return -1
        return f[amount]
            
