#working on list types
grocery = list(('groundnut', 'peanut', 'chicken', 'fruits'))

foodstuff = ['rice','egg','yam','meat']

grocery.append('toothpaste')
print(grocery)

grocery.extend(foodstuff)
print(grocery)
grocery.insert(0, 'tissue')
print(grocery)