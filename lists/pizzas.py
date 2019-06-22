'''
You work at Len’s Slice, a new pizza joint in the neighborhood. 
You are going to use your knowledge of Python lists to organize some of your sales data.

'''

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell {} different kinds of pizza!".format(num_pizzas))

pizzas = list(zip(toppings, prices))

pizzas = sorted(pizzas, key=lambda pizza: pizza[1])

cheapest_pizza = pizzas[0]

priciest_pizza = pizzas[-1]

three_cheapest = pizzas[0:3]

print(three_cheapest)

num_two_dollar_slices = pizzas.count(2)