from math import sqrt
x = int (input('Enter a number: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
    y = (sqrt(x)) / (x**0.1666667)
    print('However, the cuberoot of ', x, 'is', y)
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))


