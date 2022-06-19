# Given a string, calculate the length of the string.

input_str =str(input("enter any asting"))
#input_str="LucidProgramming"

# 1--Standard Pythonic way:
print("the lenth of the sting is ",len(input_str))

#2-- Iterative length calculation: O(n)
def iterative_str_len(input_str):
    input_str_len = 0
    for i in range(len(input_str)):
        input_str_len += 1
    return input_str_len

# 3--Recursive length calculation: O(n)
"""
def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])
"""
print(iterative_str_len(input_str))

#print(recursive_str_len(input_str))