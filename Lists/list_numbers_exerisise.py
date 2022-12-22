#exercise 1
numbers = [value for value in range(1,21)]
print(numbers)

#exercise 2

manynumbers = [value for value in range (1,1000001)]
print(manynumbers)

#exersice 3

print(min(manynumbers))
print(max(manynumbers))
print(sum(manynumbers))

#exersise 4

odd_numbers = [value for value in range(1,21,2)]
print(odd_numbers)

#exersice 5

multiple = [value for value in range(3,31,3)]
print(multiple)

#exersice 6

cubes = []
for value in range(1,11):
    value = value**3
    cubes.append(value)
print(cubes) 

#exersice 7

cube = [value**3 for value in range(1,11)]
print(cube)