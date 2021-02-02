def menu():
    print('Option 1 EAD')
    print('Option 2 MOD')
    print('Option 3 New Mix')
    print('Option 4 Rock Bottom')

menu()
option = int(input('Pick an option.  '))

while option != 0:
    if option == 1:
        exec(open("EAD.py").read())
    elif option == 2:
        exec(open("MOD.py").read())
    elif option == 3:
        exec(open("NewMix.py").read())
    else:
        print('invalid')
    print('')
    menu()
    option = int(input('Option '))
