#exersise 1
my_teams = ["Mexico", "Argentina", "Francia", "Alemania", "Canada"]
message = "The first three cpuntries in the list are:"
print(message.title())

print(my_teams[:3])

print("Three countries from the middle of the list are:")
print(my_teams[1:4])

print("Last three countries in the list are:")
print(my_teams[2:6])

#exersise 2

pizzaz = ["pepperoni", "Mexicana", "4 cheese", "meats"]

my_friend_pizza = pizzaz[:]

print("Original list:")
print("\n")
print(pizzaz)
print(my_friend_pizza)

pizzaz.append('hawuaiian')
my_friend_pizza.append("Italian")
print (pizzaz)
print(my_friend_pizza)
print("\n")

print("My favorite pizzas are:")
for pizza in pizzaz[:]:
    print(pizza.title())

print("My friend's favorite pizzas are:")
for FriendP in my_friend_pizza[:]:
    print(FriendP.title())

#Exersise 3
print("\n")
fruits = ['Apple', 'Cucumber', 'pineapple']
for fruit in fruits[:]:
    print(fruit)
