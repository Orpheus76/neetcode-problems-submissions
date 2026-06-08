class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0] * (M + 1)

        # Initialize first row
        for c in range(M + 1):
            if weight[0] <= c:
                dp[c] = profit[0]

        for i in range(1, N):
            curRow = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]  # Result from previous row
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[c - weight[i]]
                curRow[c] = max(skip, include)
            dp = curRow

        return dp[M]
