#Main file for champer 5 IF statements

cars = ['toyota', 'kia', 'bmw', 'audi']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#inequality

requested_topping = 'Mozstaza'

if requested_topping != 'Catsup':
    print("\nHold the anchovis")


age = 18
age==18

answer = 17

if answer != 42:
    print("\nThat is not the correct answer. Please try again")

#and & or operators

# IN operator

pizzaz = ['pepperoni', 'jamon', 'carnes frias', '4 quesos']

'hawuaina' in pizzaz

users = ['mafer', 'oscar', 'maria', 'alejandro']
user = 'perenganito'

if user not in users:
    print(user.title() + ", you do not have permissions. Please contact you tema leader")


# IF-ELSE
print("\n-------------------------if else-------------------------------")
age = 17

if age >= 18:
    print("\nYou are old enough to vote.")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote.")
    print("Please register to vote as soon as your turn 18!")


age = 28

if age < 4:
    print("\nYour admission cost is $0.")
elif age < 18:
    print("\nYour admission cost is $5.")
else:
    print("\nYour admission cost is $10.")

   
#-----------------IF IN A LIST--------------------------------------
print("\n-----------------If with a lists---------------------------")
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping =='green peppers':
        print("Sorry, we are out of green pappers rigth now.")

    else:
        print("Adding " + requested_topping + ".")
    
print ("\nFinished making your pizza")


requested_toppings = ['peperoni']

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("You need to provide the toppigs for your pizza.")

print("\n")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry we do not have " + requested_topping + ".")

print("Finished making your pizza")
