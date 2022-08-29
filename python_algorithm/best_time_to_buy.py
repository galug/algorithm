import sys
a= b= 1
def maxProfit(prices: [int]) -> int:
    profit = 0
    low_price = sys.maxsize
    for i in range(len(prices)):
        low_price = min(low_price,prices[i])
        profit = max(profit, prices[i]-low_price)
    return profit
print(maxProfit([7,1,5,3,6,4]))