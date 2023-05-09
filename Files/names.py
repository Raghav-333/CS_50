# All the content of this code will be stored in 'names.txt'




# name = input("What's your name? ")
# file = open('names.txt' , "w")
# file.write(name)  # Writing our input to the file.
# file.close()  # This will close and save the file.
 
# # # Enter 'Harry' , 'Ron' , 'Hermione' as input

# # # But in this code if we enter more than one name then the previous name would be deleted from the file. 









# name = input("What's your name? ")
# file = open('names.txt' , "a")  # We changed "w" to "a" to append the data in the file and keeping the previous one as it was
# file.write(name)  # Writing our input to the file.
# file.write('\n')  
# file.close()  # This will close and save the file.
# # Enter 'Harry' , 'Ron' , 'Hermione' as input









# name = input("What's your name? ")
# with open("names.txt" , "a") as file:
#     file.write(f"{name}\n")
# file.close()
# # We could also do it like this.









# # NOW WE ARE READING THE FILE.
# with open('names.txt' , 'r') as file:
#     lines = file.readlines()
#     # The readlines() method reads the whole file line by line and returns a list
    
# for line in lines:  # Iterating over the list. 
#     print("hello," , line.rstrip())  # Using rstrip() to strip the additional newlines.






# with open('names.txt' , 'r') as file:
    # lines = file.read()  # This method reads the whole file at once.
    # print("hello, " , lines)








# name = []
# with open("names.txt") as file:
#     for line in file:
#         name.append(line.rstrip())
# for names in sorted(name):   # Print the names in alphabetical order
#     print(f"Hello, {names}")




# # WE COULD ALSO DO THE ABOVE CODE LIKE THIS.
# name = []
# with open("names.txt") as file:
#     line = file.readlines()
#     # name.append(line.rstrip())

# for names in sorted(line):
#     print(f"Hello, {names.rstrip()}")



# # WE COULD ALSO DO THE ABOVE CODE LIKE THIS.
# with open('names.txt') as file:
#     for line in sorted(file):
#         print("Hello," , line.rstrip())








# # If we want to sort the file in reverse descending order then we should use the 'reverse' keyword
# name = []
# with open("names.txt") as file:
#     for line in file:
#         name.append(line.rstrip())
# for names in sorted(name , reverse=False):   # Print the names in alphabetical order
#     print(f"Hello, {names}")



# with open('names.txt') as file:
#     for line in sorted(file , reverse=True):
#         print("Hello," , line.rstrip())