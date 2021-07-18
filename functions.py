'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''
'''
My thought process:
a) Handle negative number.
b) convert int to binary.
c) create a variable to handle increments/count of num_of_ones.
d) iterate through the binary numbers.
e) for each iteration if an iteration has str = 1, increment the value of c
'''


def count_bits(n):
    if n < 0:
        print('Please enter a number greater that 0')
    else:
        num_of_ones = 0
        binary_number = format(n,'b')
        # print(binary_number)
        for i in binary_number:
            # print(type(i))
            if i == '1' :
                num_of_ones += 1
        return num_of_ones

num = count_bits(10)
print(num)



# Alternatively
def count_bits(n):
    return bin(n).count('1') # bin() coverts an int to binary while count() returns the total count of a given element
num = count_bits(1001)
print(num)