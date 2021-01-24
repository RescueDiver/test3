def truncate(number: float, digits: int) -> float:
    pow10 = 10 ** digits
    return number * pow10 // 1 / pow10


def yes_or_no(question):  # used to start and end loop
    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return
    if reply[0] == 'n':
        return 1
    else:
        return yes_or_no("Please Enter (y/n) ")


print("Let's get started\n")

while True:  # beginning of while loop
    # EAD = (FN2(Depth-33)/.79)-33
    depth = float(input("What is your planned depth? "))
    mix = float(input("\nWhat is your Nitrox mix? ")) / 100
    FN2 = (1 - mix)
    EAD = (FN2 * (depth + 33) / .79) - 33
    EADTrunc = truncate(EAD, 3)
    print('\nYour Equivalent Air Depth is', EADTrunc, 'feet')
    print('Remember to round to the deeper depth.')
    if yes_or_no('Do you want to do another?'):
        break  # end of program

print('Done')
