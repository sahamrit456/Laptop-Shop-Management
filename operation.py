from datetime import datetime
from write import *


def selllaptop(laptop_dictionary):

    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("For Bill Generation you will have to enter the your details first: ")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    name = input("Please enter the name of the Customer: ")
    print("\n")
    phone_number = input("Please enter the phone number of the Customer: ")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("S.N. \t\tCompany name          Laptop Name              Price\t    Quantity\t\t Graphics\t\t CPU")
    print("-------------------------------------------------------------------------------------------------------------------------")
    file = open("laptops.txt", "r")
    a = 1
    for line in file:
            print(a, "\t\t"+line.replace(",", "\t\t"))
            a = a+1
    print("-------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

        # getting user purchased items
    user_sell = [] 
    while True:
            valid_id = input_id(laptop_dictionary)
            valid_quantity = input_quantity(laptop_dictionary, valid_id)
            update_file_sell(laptop_dictionary, valid_id, valid_quantity)
            laptop_company = laptop_dictionary[valid_id][0]
            laptop_name = laptop_dictionary[valid_id][1]
            user_sell_quantity = valid_quantity
            generation = laptop_dictionary[valid_id][5]
            cpu = laptop_dictionary[valid_id][4]
            replaceby_onelaptop= laptop_dictionary[valid_id][2].replace("$",'')
            total_price = int(replaceby_onelaptop)*int(user_sell_quantity)
            user_sell.append([laptop_name,laptop_company,user_sell_quantity,replaceby_onelaptop,generation,cpu,total_price])    
            shipping_cost = input("Dear user do you want to sell more?(Y/N)").upper() 
            if shipping_cost=="N":
                break
            else:
                continue
    total = 0
    shipping_cost = 1500
    for i in user_sell:
            total+=int(i[6])
    VAT = 0.13 * total
    grand_total =total+shipping_cost+VAT
    today_date_and_time = datetime.now()
    print("\n")
    print("\t \t \t \t laptop  Shop Bill ")
    print("\n")
    print("\t \t Baneshwor, Kathmandu | Phone No: 9804883079 ")
    print("\n")
    print("-------------------------------------------------------------------------")
    print("Laptop Details are:")
    print("-------------------------------------------------------------------------")
    print("Name of the Costumer:"+str(name))
    print("Contact number: "+str(phone_number))
    print("Date and time of purchase: "+str(today_date_and_time), )
    print("-------------------------------------------------------------------------")
    print("\n")
    print("Purchase Detail are:")
    print("------------------------------------------------------------------------------------------------------------------")
    print("S.N. \t\tCompany name          Laptop Name              Price\t    Quantity\t\t Graphics\t\t CPU")
    print("------------------------------------------------------------------------------------------------------------------")
    for i in user_sell:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3],"\t",i[4],"\t\t",i[5])
    print("------------------------------------------------------------------------------------------------------------------")
    if shipping_cost:
            print("Your Shipping Cost is:", shipping_cost)
            print("Your VAT Cost is:", VAT)
            print("Total: $"+str(grand_total))
            print("Note: Shipping cost is added to the grand total")
    else:
            print("Total: $"+str(grand_total))
    print("\n")
    
    sell_write(name, phone_number,today_date_and_time,user_sell,shipping_cost,VAT,grand_total)


def input_id(laptop_dictionary): 
    """ Input valid id from the user."""
    valid_id = int(input("Please Provide the ID of the Laptop you want to buy: "))
    print("\n")

    # Valid ID

    while valid_id <= 0 or valid_id > len(laptop_dictionary):

        print("Please provide a valid Laptop ID !!!")

        print("\n")

        valid_id = int(input("Please Provide the ID of the laptop you want to buy:"))

        print("\n")
    return valid_id

def input_quantity_sell(laptop_dictionary, valid_id):
    """ Input valid quantity from the user."""
    # Valid Quantity
    user_quantity_sell = int(input("Enter the product quantity: "))
    get_quantity_of_selected_laptop = laptop_dictionary[valid_id][3]

    while user_quantity_sell <= 0 or user_quantity_sell > int(get_quantity_of_selected_laptop):

        print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the table and enter the quantity.")

        print("\n")

        user_quantity_sell = int(input("Please Provide the number of quantity of the Laptop you want to buy: "))
        print("\n")
    return user_quantity_sell








def buylaptop(laptop_dictionary):

    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("For Bill Generation you will have to enter the your details first: ")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    name = input("Please enter the name of the Customer: ")
    print("\n")
    phone_number = input("Please enter the phone number of the Customer: ")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("\n")

    
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("S.N. \t\tCompany name          Laptop Name              Price\t    Quantity\t\t Graphics\t\t CPU")
    print("-------------------------------------------------------------------------------------------------------------------------")
    file = open("laptops.txt", "r")
    a = 1
    for line in file:
            print(a, "\t\t"+line.replace(",", "\t\t"))
            a = a+1
    print("-------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    

        # getting user purchased items
    user_buy = [] 
    while True:
            valid_id = input_id(laptop_dictionary)
            valid_quantity = input_quantity(laptop_dictionary, valid_id)
            update_file_buy(laptop_dictionary, valid_id, valid_quantity)
            laptop_company = laptop_dictionary[valid_id][0]
            laptop_name = laptop_dictionary[valid_id][1]
            user_buy_quantity = valid_quantity
            generation = laptop_dictionary[valid_id][5]
            cpu = laptop_dictionary[valid_id][4]
            replaceby_onelaptop= laptop_dictionary[valid_id][2].replace("$",'')
            total_price = int(replaceby_onelaptop)*int(user_buy_quantity)
            user_buy.append([laptop_name,laptop_company,user_buy_quantity,replaceby_onelaptop,generation,cpu,total_price])    
            shipping_cost = input("Dear user do you want to buy more?(Y/N)").upper() 
            if shipping_cost=="N":
                break
            else:
                continue
    total = 0
    shipping_cost = 1500
    for i in user_buy:
            total+=int(i[6])
    VAT = 0.13 * total
    grand_total =total+shipping_cost+VAT
    today_date_and_time = datetime.now()
    print("\n")
    print("\t \t \t \t laptop  Shop Bill ")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255 ")
    print("\n")
    print("-------------------------------------------------------------------------")
    print("laptop Details are:")
    print("-------------------------------------------------------------------------")
    print("Name of the Costumer:"+str(name))
    print("Contact number: "+str(phone_number))
    print("Date and time of purchase: "+str(today_date_and_time), )
    print("-------------------------------------------------------------------------")
    print("\n")
    print("Purchase Detail are:")
    print("------------------------------------------------------------------------------------------------------------------")
    print("company         \t\t name               \t\tquantity \t\tUnit Price     \t\tcpu     \t\tgeneration\n")
    print("------------------------------------------------------------------------------------------------------------------")
    for i in user_buy:
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
    print("------------------------------------------------------------------------------------------------------------------")
    if shipping_cost:
            print("Your Shipping Cost is:", shipping_cost)
            print("Your VAT Cost is:", VAT)
            print("Total: $"+str(grand_total))
            print("Note: Shipping cost is added to the grand total")
    else:
            print("Total: $"+str(grand_total))
    print("\n")
    
    buy_write(name, phone_number,today_date_and_time,user_buy,shipping_cost,VAT,grand_total)

def input_idb(laptop_dictionary): 
    """ Input valid id from the user."""
    valid_id = int(input("Please Provide the ID of the Laptop you want to buy: "))
    print("\n")

    # Valid ID

    while valid_id <= 0 or valid_id > len(laptop_dictionary):

        print("Please provide a valid Laptop ID !!!")

        print("\n")

        valid_id = int(input("Please Provide the ID of the laptop you want to buy:"))

        print("\n")
    return valid_id


def input_quantity(laptop_dictionary, valid_id):
    """ Input valid quantity from the user."""
    # Valid Quantity
    user_quantity = int(input("Enter the product quantity: "))
    get_quantity_of_selected_laptop = laptop_dictionary[valid_id][3]

    while user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_laptop):

        print("Dear Admin, the quantity you looking for is not available in our shop. Please look again in the table and enter the quantity.")

        print("\n")

        user_quantity = int(input("Please Provide the number of quantity of the Laptop you want to buy: "))
        print("\n")
    return user_quantity
