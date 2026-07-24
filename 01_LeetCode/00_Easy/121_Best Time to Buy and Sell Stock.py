def max_profit(prices):
    min_price = float('inf')
    profit_max = 0

    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > profit_max:
            profit_max = price - min_price
    return profit_max


prices1 = [7,1,5,3,6,4]
print(max_profit(prices1))