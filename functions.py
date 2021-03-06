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
# def count_bits(n):
#     if n < 0:
#         print('Please enter a number greater that 0')
#     else:
#         num_of_ones = 0
#         binary_number = format(n,'b')
#         # print(binary_number)
#         for i in binary_number:
#             # print(type(i))
#             if i == '1' :
#                 num_of_ones += 1
#         return num_of_ones

# num = count_bits(10)
# print(num)


# # Alternatively
# def count_bits(n):
#     return bin(n).count('1') # bin() coverts an int to binary while count() returns the total count of a given element
# num = count_bits(1001)
# print(num)


'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

'''
# import string
# def is_pangram(str):
#     alphabet = string.ascii_lowercase
#     for char in alphabet:
#         if char not in str.lower():
#             return False
#     return True


# ans = is_pangram("This isn't a pangram!")

# print(ans)


'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes:
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

'''


def high_and_low(numbers):  # z.
    nn = [int(s) for s in numbers.split(" ")]
    print(nn)
    print(numbers.split())
    return "%i %i" % (max(nn), min(nn))


print(high_and_low('1 2 -3 4 -5'))

# alternatively.

def high_and_low(numbers):
    n = list(map(int, numbers.split(' ')))
    print(n)
    return str(max(n)) + ' ' + str(min(n))


print(high_and_low('1 2 -3 4 -5'))