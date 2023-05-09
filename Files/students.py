# ALL OF THE DATA OF THIS FILE IS STORED IN 'STUDENTS.CSV'
# 'csv' stands for 'comma separated values' is a delimited text file that uses comma for separation.



# with open('students.csv') as file:
#     for line in file:
#         row = line.rstrip().split(',')
#         print(f"{row[0]} is in {row[1]}")








# with open('students.csv') as file:
#     for line in file:
#         name , house = line.rstrip().split(',')
#         # 'name' holds the value for row[1]
#         # 'house' holds the value for row[2]
#         print(f"{name} is in {house}")







# # BELOW IS THE CODE TO PRINT THE TEXT IN ALPHABETICAL ORDER
# students = []

# with open('students.csv') as file:
#     for line in file:
#         name , house = line.rstrip().split(',')
#         students.append(f"{name} is in {house}")
# for student in sorted(students):
#     print(student)
    
    
    
    
    
    


# students = []
# with open('students.csv') as file:
#     for line in file:
#         name , house = line.rstrip().split(',')
#         student = {}
#         student["name"] = name 
#         student["house"] = house 
#         students.append(student)
#     # print(students)
    
# for lst in students:
#     print(f"{lst['name']} is in {lst['house']}")  
#     # A dictionary in inside the list 'students'
#     # We could access value of 'name' key by the above syntax









# # SORTING THE LIST BY THE 'name' OF THE STUDENTS
# students = []
# with open('students.csv') as file:
#     for line in file:
#         name , house = line.rstrip().split(',')
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)
#     # print(students)
    

# def get_name(student): # It's use is to return the 'name'
#     return student['name']  # 'student' is a dictonary

# for lst in sorted(students , key=get_name):
#     print(f"{lst['name']} is in {lst['house']}")  
#     # Jab hamne 'students' mein 'key' parameter ko 'get_name' function dala toh usne 'students' list mein jo dictionary hai uski 'key' ke hisaab se puri list ko sort kara.











# # SORTING THE LIST BY THE 'house' OF THE STUDENTS
# students = []
# with open('students.csv') as file:
#     for line in file:
#         name , house = line.rstrip().split(',')
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)
#     # print(students)

# def get_house(student): # It's use is to return the 'house'
#     return student['house']  # 'student' is a dictonary

# for lst in sorted(students , key=get_house):
#     print(f"{lst['name']} is in {lst['house']}")  
#     # Jab hamne 'students' mein 'key' parameter ko 'get_house' function dala toh usne 'students' list mein jo dictionary hai uski 'key' ke hisaab se puri list ko sort kara.