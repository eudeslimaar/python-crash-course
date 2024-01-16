my_pizzas = ['pepperoni', 'pineapple', 'mushrooms']
my_pizzas.append('cheese')
friend_pizzas = my_pizzas[:]
friend_pizzas.append('ham')

for pizza in my_pizzas:
    print(f'My favorite pizzas are: {pizza}')

for pizza in friend_pizzas:
    print(f"My friend’s favorite pizzas are: {pizza}")
