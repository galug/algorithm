import sys
def maxProfit(prices: [int]) -> int:
    profit = 0
    minprice, maxprice = sys.maxsize, 0

    for i in range(len(prices) - 1):
        # changing max_profit occur inflection point
        if prices[i+1] > prices[i]:
            minprice = min(prices[i], minprice)
            profit = max(profit, prices[i+1] - minprice)

    return profit
print(maxProfit([7,1,5,3,6,4]))