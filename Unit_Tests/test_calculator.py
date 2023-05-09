from calculator import square



# def main():
#     test_square()
    
# def test_square():
#     if square(2) != 4:
#         print('2 squared was not 4') 
#     if square(3) != 9:
#         print('3 squared was not 9')
        
# if __name__ == "__main__":
#     main()








# def main():
#     test_square()
    
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
        
# if __name__ == "__main__":
#     main()
# # We could use 'assert' function in place of various if statements
# #  'assert' function returns nothing if the condition is true and it returns an 'AsssertionError' if the condition evaluated to false.
# # We will use '==' in place of '!='







# def main():
#     test_square()
    
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print('2 square was not 4')
        
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print('3 square was not 9')
        
# if __name__ == "__main__":
#     main()









# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0
# # We could just use 'pytest' module to check if the above tests are passed or not.











# # IT COULD BE A GOOD WAY TO TEST THE 'POSITIVE' NUMBERS SEPARATELY AND MY 'NEGATIVE' NUMBERS SEPARATELY AND '0' SEPARATELY
# # Even if one of the test cases in one of the function fails, the other function will be executed
# # It will help us to find the clue of the problem

# def test_positive():
#     assert square(2) == 4 
#     assert square(3) == 9
# def test_negative():
#     assert square(-2) == 4
#     assert square(-3) == 9
# def test_zero():
#     assert square(0) == 0
# # All three functions will be run automatically.








# import pytest

# # If we enter a string value or any value different of the given type then we should use a function from 'pytest' named 'pytest.raises' to raise a specefic error and pass the test cases
# def test_positive():
#     assert square(2) == 4 
#     assert square(3) == 9
# def test_str():
#     with pytest.raises(TypeError):
#         assert square("cat")