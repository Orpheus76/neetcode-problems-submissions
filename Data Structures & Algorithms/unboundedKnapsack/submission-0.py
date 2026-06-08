class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # dp[c] stores the max profit for capacity 'c'
        dp = [0] * (capacity + 1)

        # Iterate through each item
        for i in range(len(profit)):
            # Update the dp array for each capacity from weight[i] to capacity
            for c in range(weight[i], capacity + 1):
                # Max of (not taking the item) vs (taking the item + profit of remaining capacity)
                dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])

        return dp[capacity]
