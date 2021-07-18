from math import sqrt
try:
    x = int (input('Enter a number: '))
except ValueError as err:
    print('Please enter a number!!\n ')
    x = int(input('Enter a number: '))

'''
Now we creat a loop that generates guesses 
'''
ans = 0
x = abs(x)
while ans**3 < (x):
    ans = ans + 1

#write a code that says if ans**3 is not equal to watever the user inputs, perform the cuderoot of that number
if ans**3 != (x):
    print(str(x) + ' is not a perfect cube')
    y = (sqrt(x)) / (x**0.1666667)
    print('However, the cuberoot of ', x, 'is', y)
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))


