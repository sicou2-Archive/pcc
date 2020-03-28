my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
#This does not work
#friend_foods = my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#4_12 More loops

print("My favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)
