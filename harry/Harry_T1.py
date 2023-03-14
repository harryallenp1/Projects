# Harry Allen
# ID : 991680235
eligible_users = []

while True:
    # user input foe the userDetails
    print("----------------------------------------------------")
    print("\n")
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    has_speeding_ticket = input("Have you received a speeding ticket in the past? (Yes/No) ").lower() == "yes"
    
    # To fond out the eligiblity  and the premium amount as per the given criteria
    if age >= 25:
        if not has_speeding_ticket:
            premium = 500
            eligible = True
        else:
            premium = 1000
            eligible = True
    else:
        has_taken_driving_course = input("Have you taken a driving course? (Yes/No) ").lower() == "yes"
        if not has_speeding_ticket:
            if has_taken_driving_course:
                premium = 1000
                eligible = True
            else:
                premium = 1500
                eligible = False
        else:
            if has_taken_driving_course:
                premium = 1500
                eligible = True
            else:
                eligible = False
    
    # To display the eligiblity status
    if eligible:
        print("Your Premium amount would be ${}.".format(premium))
        print("----------------------------------------------------")
        print("\n")
        eligible_users.append(name)
    else:
        print("Sorry, you are not eligible for insurance coverage.")
        print("----------------------------------------------------")
        print("\n")
    # to input the next user
    another_person = input("Do you want to check eligibility for another person? (Yes/No) ").lower() == "yes"
    print("\n")
    print("----------------------------------------------------")
    if not another_person:
        break

# to display list of eligible users
if eligible_users:
    print("The following users are eligible for insurance coverage: ")
    for user in eligible_users:
        print("- {}".format(user))
        print("\n")
else:
    print("No users are eligible for insurance coverage.")
    print("\n")
    
print("----------------------------------------------------")
    