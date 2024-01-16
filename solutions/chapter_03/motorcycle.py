motorcycles = [
    'honda',
    'yamaha',
    'suzuki'
]
print('original: ', motorcycles)
# motorcycles[0] = 'ducati'
motorcycles.append('ducati')
motorcycles.insert(0, 'royal enfield')
print('Modified: ', motorcycles)
del motorcycles[0]
print('Modified: ', motorcycles)

popped_motorcycle = motorcycles.pop()
print('Popped motorcycle: ', popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

