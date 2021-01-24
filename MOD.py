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


print("Let's get started")

while True:  # beginning of while loop
    # blend = float(input('What is your mix   ')) / 100  # What is the Nitrox blend
    while True:  # blend range loop
        try:
            blend = float(input('What is your mix? ')) / 100  # What is the Nitrox blend
            if blend < .001 or blend > 1:
                raise ValueError  # if out of the range it starts a loop
            break
        except ValueError:
            print("The number must be in the range of 10 to 100.")
        # PO2 = float(input('What is your PO2, 1.4, 1.5, 1.6? '))  # What is your PO2
    while True:  # PO2 range loop
        try:
            PO2 = float(input('What is your PO2, 1.4, 1.5, 1.6? '))  # What is your PO2
            if PO2 < 1.0 or PO2 > 1.6:
                raise ValueError  # if out of the range it starts a loop
            break
        except ValueError:
            print("The number must be in the range of 1.0 to 1.6.")
    MOD = ((PO2 / blend) - 1) * 33
    MODT = truncate(MOD, 3)
    print('Max Depth for ', blend * 100, 'is', MODT)

    if yes_or_no('Do you want to do another?'):
        break  # end of program

print("done")
