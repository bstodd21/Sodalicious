print("Welcome to Sodalicious!! So happy to see you today!!")

answer = input("Would you like a custom soda? ")

if answer == 'Yes':
    print("Let's get that order started then!!!")
elif answer == 'No':
    print("Have a good day!!")
    quit()
else:
    for x in answer:
        print("I'm sorry, that wasn't the answer we were looking for.")
        answer = input("Would you like a custom soda? ")
        if answer == 'Yes':
            print("Let's get that order started then!!!")
        break

soda_choice = input("What soda would you like? ")

for y in range(1):
    flavor_choice = input("What flavor would you like? ")
    flavor_choice2 = input("What other flavor would you like? ")
    flavor_choice3 = input("What other flavor would you like? ")
    if flavor_choice2 == "None":
        continue
    elif flavor_choice3 == "None":
        break
    else:
        continue

if flavor_choice != 'None' and flavor_choice2 == 'None' and flavor_choice3 == 'None':
    print(f"Here is your {soda_choice} with {flavor_choice}.")
elif flavor_choice2 != 'None' and flavor_choice3 == 'None':
    print(f"Here is your {soda_choice} with {flavor_choice}, and {flavor_choice2}.")
elif flavor_choice3 != 'None' and flavor_choice2 == 'None':
    print(f"Here is your {soda_choice} with {flavor_choice}, and {flavor_choice3}.")
else:
    print(f"Here is your {soda_choice} with {flavor_choice}, {flavor_choice2}, and {flavor_choice3}.")

print("Thank your for coming!! Have a great day!!")
