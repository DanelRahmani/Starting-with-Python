empty_tuple = tuple()
brothers = ('Aryan', 'Khesraw')
parents = ('Taher', 'Ghazal')
family_members = (brothers + parents)
print(f'you have {len(family_members)} close family members')

brother1, brother2, parent1, parent2 = family_members
print(brother1, brother2, parent1, parent2)

fruits = ('Apple', 'Banana', 'Mango', 'Watermelon', 'Strawberry')
vegetables = ('Broccoli', 'Cucumber', 'Paprika', 'Onion', 'Beans')
animal_products = ('Milk', 'Cheese', 'Beef', 'Eggs', 'Chicken')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt= list(food_stuff_tp)
middle_item = food_stuff_tp[(len(food_stuff_tp)//2)]
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-4:-1]
print(middle_item, first_three, last_three)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(f'Estonia is a Nordic Country is : {'Estonia' in nordic_countries}')
print(f'Iceland is a Nordic Country is : {'Iceland' in nordic_countries}')
