bycicles = ['trek', 'cannondale', 'redline', 'specialized']

print(bycicles[0].title())
print(bycicles[-2].title())
print(' ')


##/////// EXERCISE ///////////////

friends = ['cano', 'culio', 'melman', 'patron']

#1
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(' ')


#2

message = 'El ' + friends[0].title() + ' siempre la caga'

print(message)


message = 'El ' + friends[1].title() + ' siempre la caga'

print(message)

message = 'El ' + friends[2].title() + ' siempre la caga'

print(message)

message = 'El ' + friends[3].title() + ' siempre la caga'

print(message)

print(' ')

cars = ['mercedes-benz', 'ferrari', 'mclaren']

message = 'Some day I will have a ' + cars[0].title()

print(message)


#----------------Changing a value from the list


print(cars)

cars[2] = 'VMW'

print(cars)


# add new elemnt ot the end of the list 

cars.append('Alfa Romeo')

print(cars)


#---------- Using an empty list let's add elements --------------


countries = []

countries.append('mexico')
countries.append('canada')
countries.append('usa')
countries.append('chile')
countries.append('venezuala')

print(countries)


#---------- Adding the new value in a specific position

countries.insert(0, 'colombia')

print(countries)


#------ Remove a specific value from the list ------------

del countries[0]

print(countries) 

#Removing something from a list with POP method

popped_countries = countries.pop(0)
print(countries)

print(popped_countries)

#------ Remove method ---------------

small_one = 'venezuala'
countries.remove(small_one)

print(countries)
print('\n' + small_one.title() + ' is the smallest country in the list' )


#-------------SORT() METHOD PERMATHLY SORTED
countries.sort()
print()
print(countries)


countries.sort(reverse=True)
print(countries)


#-------------SORTED() METHOD TEMPORARILY SORTED

print('\nHere is the original list:')
print(countries)

print("This is the sorted list:")
print(sorted(countries))

print('\nHere is the original list again:')
print(countries)

countries.sort(reverse=True)

print (countries)

#--------length of a list


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
len(cars)



#----------TUPLES 
print("\n------------ Dimensions -------------")
print("\n")
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
print("\nLooping tuple")
for dimension in dimensions:
    print(dimension)

print("\nWriting over a tuple")
print("Orginal tuple:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("New tuple values:")
for dimension    in dimensions:
    print(dimension)