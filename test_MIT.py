x = float(input('Enter a value: '))
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('divisible by 2 and not by 3')
elif x % 3 == 0:
    print('Divisible by 3 and not by 2')
else:
    print('not divisible by 2 and 3\n ')
    y = x/2
    z = x/3
    print('Your answer is: \nDivided by 2 = ', y , '\nDivided by 3 = ', z )
    
