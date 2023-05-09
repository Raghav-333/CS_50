def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    for i in s[2:]:
        if i.isalpha() == False or i.isdigit() == True:
            return False
    if s.isalpha() == False or s.isdigit == False:
        return False
    for iter in s:
        if iter.isdigit() == True:
            if iter == 0:
                return False
            ind = str.index(iter)
            value = str[ind:]
            if value.isdigit() == False:
                return False
    return True
    
main()
