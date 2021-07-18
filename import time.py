import time
'''
This is a car game

'''
start = 0
print('#'*70)

begin = input('Enter Help to see instructions: ')

if begin == 'Help' or 'help':
    import time
'''
This is a car game

'''
start = 0
print('#'*70)

begin = input('Enter Help to see instructions: ')

if begin == 'Help' or 'help':
    print('Type Start to Begin\n \nType Stop to End game\n ')
else:
    exit()

move = input('\nType Start to Move the game: ')
if move == 'Stop' or 'stop':
    print('Car stopped')
    exit()
elif move != 'Start' or 'start':
    while move == 'Start' or 'start':
        print('Car is moving...........')
        time.sleep(2)
        start += 1
        if start > 5:
            print('Out of Gas!!!!!\nCar Stopped')
            exit()

else:
    exit()
else:
    exit()

move = input('\nType Start to Move the game: ')

if move != 'Start' or 'start':
    while move == 'Start' or 'start':
        print('Car is moving...........')
        time.sleep(2)
        start += 1
        if start > 5:
            print('Out of Gas!!!!!\nCar Stopped')
            exit()









    
