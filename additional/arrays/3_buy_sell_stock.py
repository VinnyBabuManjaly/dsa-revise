"""Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Brute Force: try all possible pairs of buy and sell days and calculate the profit for each pair. 
             Then, you return the maximum profit found.


Approach: Greedy + One-Pass Minimum Tracking
At each point, it takes the optimal action based on current and past info
keep track of min price and max profit at each step
    - if price<min price, update min price
    - else means there is a profit, so update max profit as max of max profit or (max profit-min price)
return profit

time complexity - O(n) - single run
space complexity - O(1) - constant extra memory
"""

class BuySellStockSolver:
    def buy_sell_stock(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices: 
            if price < min_price:
                min_price = price
            else: 
                max_profit = max(max_profit, price - min_price)
        return max_profit
    

if __name__ == "__main__":
    solver = BuySellStockSolver()
    prices = [7,1,5,3,6,4]
    result = solver.buy_sell_stock(prices)
    print(result)

