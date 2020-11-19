# Len's Slice Codecademy project
# 11/19/2020

# list of toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# length of toppings list or number of pizzas
num_pizzas = len(toppings)

# print # of pizzas
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

# combine pizzas and prices into pizzas list
pizzas = list(zip(prices, toppings))

print(pizzas)
print('')

# sort pizzas by price
pizzas.sort()

print('Sorted:')
print(pizzas)
print('')

# find cheapest pizza
cheapest_pizza = pizzas[0]

print('Cheapest:')
print(cheapest_pizza)
print('')

# find priciest pizza
priciest_pizza = pizzas[-1]

print('Priciest:')
print(priciest_pizza)
print('')

# find three cheapest pizzas
three_cheapest = pizzas[:3]

print('Three Cheapest:')
print(three_cheapest)
print('')

# find number of $2 slices
num_two_dollar_slices = prices.count(2)

print('Number of $2 slices:')
print(num_two_dollar_slices)
