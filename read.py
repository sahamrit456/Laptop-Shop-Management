def read1():
    file = open("laptops.txt", "r")
    laptop_dictionary = {}
    laptop_id = 1
    for line in file:
        line = line.replace("\n", "")
    laptop_dictionary.update({laptop_id: line.split(",")})
    laptop_id = laptop_id + 1
    file.close()