from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        i = 0
        while i < n - 1:
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
            i += 1
        return profit


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 7
    assert solution.maxProfit(prices=[1, 2, 3, 4, 5]) == 4
