# 'command line arguments' allows you to enter input not when prompted inside a program but when we are executing at the command line.
# You can provide any number of words or numbers or phrases after the command.



import sys

# To use this type 'cd Libraries'
# Then type 'python library_cla.py [input]'



# print('Hello , my name is' , sys.argv[0])
# # We type 'sys.argv[1]' because at index '0' there is the name of file.
# # This would print the name of the file.






# try:
#     print('Hello , my name is' , sys.argv[1])
# except IndexError:
#     print('Too few arguments')
# # We are doing this because if we nothing then we would get a string rather than an error.







# if len(sys.argv) < 2:  # The two argument would be the name of the program and the name of the human
#     print('Too few arguments')
# elif len(sys.argv) > 2:  
#     print('Too many arguments')
# else:  
#     print('Hello , my name is' , sys.argv[1])








# # if len(sys.argv):
# #     print('Too few arguments')
# # elif len(sys.argv) > 2:  
# #     print('Too many arguments')
# # # If we run the above code we would the the print statements but we would also see the 'IndexError' if the value is wrong.
#         #  ↓
#         #  ↓
# if len(sys.argv):
#     sys.exit('Too few arguments')
# elif len(sys.argv) > 2:  
#     sys.exit('Too many arguments')
    
# # 'sys.exit' is just like 'break' and it can end the program if the condition evaluated to true.







# Input:- Raghav Athak Aaradhya
if len(sys.argv) < 2:
    sys.exit('Too few arguments')
# 
# for arg in sys.argv:
#     print('Hello , my name is' , arg) # If we run this code we will also get the name of the file
# 
for arg_slice in sys.argv[1:]:
    print('Hello , my name is' , arg_slice)