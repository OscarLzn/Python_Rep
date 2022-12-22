#exersise 1
dinner_list = ['Ronaldo', 'Ronaldinho', 'Messi', 'Method Man', 'Redman']

print('Hi ' + dinner_list[0].title() + ', your are part of this family come to our dinner')

print('Hi ' + dinner_list[3].title() + ', I never met you, I would like to know about you, we would like to have you here :)')


print(dinner_list[2] + ' , come to our dinner this friday')

#exersise 2

print('\n' + dinner_list[2] + ' could not be able to join to our dinner')

dinner_list[2] = 'Nach'

print('Hi ' + dinner_list[0].title() + ', your are part of this family come to our dinner')

print('Hi ' + dinner_list[3].title() + ', I never met you, I would like to know about you, we would like to have you here :)')


print(dinner_list[2] + ' , come to our dinner this friday')

#exersise 3

dinner_list.insert(0, 'zpu')
dinner_list.insert(3, 'Rapsus')
dinner_list.append('KaseO')

print(dinner_list)

print('\nHi ' + dinner_list[0].title() + ', your are part of this family come to our dinner')

print('Hi ' + dinner_list[3].title() + ', I never met you, I would like to know about you, we would like to have you here :)')


print(dinner_list[7] + ' , come to our dinner this friday')

#exersise 4

print('\nI can only invite 2 persons to the dinner, tables is not available for all persons')

person = dinner_list.pop()

print('Sorry ' + person.title() + " , we will reschedule the dinner, table in the restaurat won't be available this time")

person = dinner_list.pop()

print('Sorry ' + person.title() + " , we will reschedule the dinner, table in the restaurat won't be available this time")

person = dinner_list.pop()

print('Sorry ' + person.title() + " , we will reschedule the dinner, table in the restaurat won't be available this time")

person = dinner_list.pop()

print('Sorry ' + person.title() + " , we will reschedule the dinner, table in the restaurat won't be available this time")

person = dinner_list.pop()

print('Sorry ' + person.title() + " , we will reschedule the dinner, table in the restaurat won't be available this time")

person = dinner_list.pop()

print('Sorry ' + person.title() + " , we will reschedule the dinner, table in the restaurat won't be available this time")

del dinner_list[0]
del dinner_list[0]

print(dinner_list)
