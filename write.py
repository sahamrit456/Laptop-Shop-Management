
def sell_write(name,phone_number,today_date_and_time, user_sell,shipping_cost,VAT, grand_total):
    # today_date_and_time = datetime.now()
    with open(str(name)+str(phone_number)+".txt", "w") as file:
            file.write("\n")
            file.write("\t \t \t \t Laptop  Shop Bill ")
            file.write("\n")
            file.write("\t \t Baneshwor, Kathmandu | Phone No: 9804883079 ")
            file.write("\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("Laptop Details are:\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("Name of the Costumer: "+str(name)+"\n")
            file.write("Contact number: "+str(phone_number)+"\n")
            file.write("Date and time of purchase: "+str(today_date_and_time)+"\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Purchase Detail are:\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("company         \t\t name               \t\tquantity \t\tUnit Price     \t\tcpu     \t\tgeneration\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            for i in user_sell:
                file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t\t\t    "+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+str(i[4])+"\t\t\t"+str(i[5])+"\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            if shipping_cost:
                file.write("Your Shipping Cost is:"+""+str(shipping_cost)+"\n")
                file.write("Your VAT Cost is:"+""+str(VAT)+"\n")
                file.write("\n")
                file.write("Total: $"+str(grand_total)+"\n")
                file.write("\n")
                file.write("          ****Note: Shipping cost is added to the grand total****"+"\n")
                file.write("\n")
            else:
                file.write("Grand Total: $"+str(grand_total))
            print("\n")

def update_file_sell(laptop_dictionary, valid_id, valid_quantity):
    """ Updates the text file."""
    # Update the text file

    laptop_dictionary[valid_id][3] =  int(laptop_dictionary[valid_id][3])-int(valid_quantity)

    file = open("laptops.txt", "w")

    for value in laptop_dictionary.values():
        file.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4])+","+str(value[5]))
        file.write("\n")
    file.close()


def buy_write(name,phone_number,today_date_and_time, user_buy,shipping_cost,VAT, grand_total):
    # today_date_and_time = datetime.now()
    with open(str(name)+str(phone_number)+".txt", "w") as file:
            file.write("\n")
            file.write("\t \t \t \t Laptop  Shop Bill ")
            file.write("\n")
            file.write("\t \t Baneshwor, Kathmandu | Phone No: 9804883079 ")
            file.write("\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("Laptop Details are:\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("Name of the Costumer: "+str(name)+"\n")
            file.write("Contact number: "+str(phone_number)+"\n")
            file.write("Date and time of purchase: "+str(today_date_and_time)+"\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Purchase Detail are:\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("company         \t\t name               \t\tquantity \t\tUnit Price     \t\tcpu     \t\tgeneration\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            for i in user_buy:
                file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t\t\t    "+str(i[2])+"\t\t\t"+"$"+str(i[3])+"\t\t\t"+str(i[4])+"\t\t\t"+str(i[5])+"\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            if shipping_cost:
                file.write("Your Shipping Cost is:"+""+str(shipping_cost)+"\n")
                file.write("Your VAT Cost is:"+""+str(VAT)+"\n")
                file.write("\n")
                file.write("Total: $"+str(grand_total)+"\n")
                file.write("\n")
                file.write("            ****Note: Shipping cost is added to the grand total****"+"\n")
                file.write("\n")
            else:
                file.write("Grand Total: $"+str(grand_total))
            print("\n")


            
def update_file_buy(laptop_dictionary, valid_id, valid_quantity):
    """ Updates the text file."""
    # Update the text file

    laptop_dictionary[valid_id][3] =  int(laptop_dictionary[valid_id][3])+int(valid_quantity)

    file = open("laptops.txt", "w")

    for value in laptop_dictionary.values():
        file.write(str(value[0])+","+str(value[1])+","+str(value[2])+","+str(value[3])+","+str(value[4])+","+str(value[5]))
        file.write("\n")
    file.close()