# Carly's Clippers project for Codecademy
# Initial code 11/19/2020

# hairstyles: names and cuts offered
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# prices: price of each hairstyle in hairstyles
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# last_week: number of each hairstyle purchased last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Find average price
total_price = 0
for price in prices:
    total_price += price

average_price = total_price / int(len(prices))

# Print average price
print('Average Haircut Price: $' + str(average_price))

# Lower all prices by 5 w/ list comprehension
new_prices = [price - 5 for price in prices]

print(new_prices)

# Find total revenue for the week
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print('Total Revenue: $' + str(total_revenue))

# Find average daily revenue
average_daily_revenue = total_revenue / 7

print('Average Daily Revenue: $' + str(average_daily_revenue))

# Print all haircuts that are under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(cuts_under_30)
