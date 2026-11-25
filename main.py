""" A Python program that finds the best single buy-sell profit by tracking the lowest price seen so far and updating 
the maximum profit whenever a better selling opportunity appears."""

prices = [7, 1, 3, 5, 9, 12]

minPrice = prices[0]
maxProfit = 0
price = 0

for price in prices:
    if price < minPrice:
        minPrice = price
    elif price-minPrice>maxProfit:
            maxProfit=price-minPrice
            
    print(f"Max Profit: {maxProfit}")