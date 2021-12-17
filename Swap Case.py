def swap_case(s):
    print('This is  the first solution')
    return s.swapcase()


# if __name__ == "__main__":
#     #s = input()
#     #result = swap_case(s)
#     print(result)


def swap_case(s):
    print('This is  the second solution')
    for i in s:
        if i.isupper():
            print(i.lower(), end='')
        else:
            print(i.upper(), end='')

#swap_case('Hello World')

