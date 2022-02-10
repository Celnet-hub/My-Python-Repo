import re
def arithmetic_arranger(problems):
    # check if the input is a valid input
    for problem in problems:
        if (re.search("[^\s0-9.+-]", problems)):
            return "Error: Only numbers are allowed"
        elif (re.search("[/]", problems) or re.search("[*]", problems)):
            return "Error: Operator not allowed"
        else:


    # return arranged_problems


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])





