#Exersise 1

users = ['Oscar','Juan','Diana','Ana', 'Admin']

if users:
    for user in users:
        if user == 'Admin':
            print("Hello Admin, would you like to see a status report?")
        else:
            print("Hello " + user)
else:
    print("We need to find some users!")


current_users = ['Oscar','Juan','Diana','Ana', 'Admin']
new_users = ['Maria','ana','Pedro','Carlos','fatima']

lower_curr_usr = [i.lower() for i in current_users] # Making a new list with names in lower case

for new_user in new_users:
    if new_user.lower() in lower_curr_usr:
        print("ERROR, User name: " + new_user + " already exist, please try another user name.")
    else:
        print("User " + new_user + " was successfully created.")


#Exersise 

print("------------------- Ordinal numbers ---------------------------------")

ordinal = ['1','2','3','4','5','6','7','8','9']

for i in ordinal:
    if i == '1':
        print(i+"st")
    elif i == '2':
        print(i+"nd")
    elif i == '3':
        print(i+"rd")
    else:
        print(i+"th")
