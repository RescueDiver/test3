import time
from time import sleep  # for making pause


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
    depth = float(input('Whats your max Depth   '))  # input for depth
    PO2 = float(input('What is your PO2, 1.4, 1.5, 1.6? '))  # What is your PO2
    ata = ((depth / 33) + 1)  # convert depth to actual total atmospheres
    mix = (PO2 / ata) * 100
    # Blank line
    print('Let me think about that')
    print('You really should be doing this math yourself')
    sleep(1)
    # Blank line
    print('Best Mix  ', mix)
    if yes_or_no('Do you want to do another?'):
        break
print("done")
