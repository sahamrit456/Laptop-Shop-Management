import operation 

print("\n")
print("\n")
print("\t \t \t \t \t \t Janakpur Electronics ")
print("\n")
print("\t \t \t \t \tBaneshwor, Kathmandu | Phone No: 9804883079 ")
print("\n")
print("-------------------------------------------------------------------------------------------------------------------------")
print("\t \t \t \t Welcome to the system Admin! I hope you have a good day!")
print("-------------------------------------------------------------------------------------------------------------------------")
print("\n")

file = open("laptops.txt", "r")
laptop_dictionary = {}
laptop_id = 1
for line in file:
    line = line.replace("\n", "")
    laptop_dictionary.update({laptop_id: line.split(",")})
    laptop_id = laptop_id + 1
file.close()

loop = True
while loop == True:
    print("-------------------------------------------------------------------------------------------")
    print("Given below are some of the options for you want the needed operations in the system")
    print("-------------------------------------------------------------------------------------------")
    print("\n")
    print("Press 1 to sale the laptop to customer.")
    print("Press 2 to buying from Manufacturer.")
    print("Press 3 to Exit from the system.")
    print("\n")
    print("-------------------------------------------------------------------------------------------")
    print("\n")

    user_input = int(input("Enter the option to continue: "))

    print("\n")

    if user_input == 1:
        operation.selllaptop(laptop_dictionary)
    elif user_input == 2:
        operation.buylaptop(laptop_dictionary)
    elif (user_input == 3):
        print("Thank you visit again")
        break  #get out of loop
    else:
        print("Invalid input. Please check and try again.")