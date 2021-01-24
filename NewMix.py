import re


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
    #  start_pressure = float(input("What is your tank pressure?(100 to 3500) "))
    while True:                         # start pressure range loop
        try:
            start_pressure = float(input("What is your tank pressure?(100 to 3500) "))
            if start_pressure < 100 or start_pressure > 4000:
                raise ValueError  # if out of the range it starts a loop
            break
        except ValueError:
            print("The number must be in the range of 100 to 3500.")
    #  start_mix = float(input('What is the mix in the tank? ')) / 100
    while True:                         # start mix range loop
        try:
            start_mix = float(input("What is your starting mix?(20.9 to 100) ")) / 100
            if start_mix < .209 or start_mix > 1:
                raise ValueError  # if out of the range it starts a loop
            break
        except ValueError:
            print("The number must be in the range of 20.9 to 100.")
    #  end_pressure = float(input('What is the final pressure you want? '))
    while True:                         # ending pressure loop
        try:
            end_pressure = float(input("What is the final pressure you want?(100 to 3500) "))
            if end_pressure < 100 or end_pressure > 4000:
                raise ValueError  # if out of the range it starts a loop
            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 100 to 3500.")
    #  topoff_mix = float(input('What mix are you topping off with? ')) / 100
    while True:                       # top off mix loop
        try:
            topoff_mix = float(input("What mix are you topping off with?(20.9 to 100) ")) / 100
            if topoff_mix < .209 or topoff_mix > 1:
                raise ValueError  # if out of the range it starts a loop
            break
        except ValueError:
            print("IThe number must be in the range of 20.9 to 100.")

    have_O2 = (start_pressure * start_mix)
    addO2 = ((end_pressure - start_pressure) * topoff_mix)
    new_mix = (((have_O2 + addO2) / end_pressure) * 100)
    NTM = truncate(new_mix, 3)
    print('Your new mix is', NTM, )
    if yes_or_no('Do you want to do another?'):
        break
print("done")
