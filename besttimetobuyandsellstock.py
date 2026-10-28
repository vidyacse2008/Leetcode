"""
Day 2 - LeetCode 121: Best Time to Buy and Sell Stock (Easy)

prices[i] is the price of a stock on day i. Pick ONE day to buy and a LATER
day to sell. Return the maximum profit you can get, or 0 if no profit is
possible.

Example 1:  prices = [7,1,5,3,6,4]  ->  5   (buy at 1, sell at 6)
Example 2:  prices = [7,6,4,3,1]    ->  0   (prices only fall, so don't trade)

Constraints:
    1 <= len(prices) <= 10^5
    0 <= prices[i] <= 10^4

Target: n can be 10^5, so a nested loop over every buy/sell pair is too slow.

Run your tests with:  pytest test_besttimetobuyandsellstock.py
"""


class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        profit=0
        for price in prices:
            profit = max(profit, price-min_price)
            min_price = min(price,min_price)
        return profit

