def yes_no(question):
    reply = str(input(question + "y/n")).lower().strip()
    if reply[0] == "y":
        return
    if reply[0] == 'n':
        return 1
    else:
        return yes_no('Please Enter y or n')


print('Rock Bottom Calculation')

while True:  # beginning of loop
    depth = float(input('What is your max depth? '))
    stop_depth = float(input('What is your Safety Stop depth? '))
    stop_time = float(input('How long is yor Safety Stop? '))
    ts = float(input('What is the Cubic Feet of your tank? '))
    tp = float(input('What is the working pressure of your tank? '))
    tankFactor = (ts / tp)
    print(tankFactor, 'PSI per cubic feet of gas')
    ata = ((depth / 33) + 1)
    print(ata)
    #  Time
    ascent_time = (((depth / 30) + stop_time) + 1)
    print(ascent_time, 'minutes until you reach the surface')
    average_depth = ((((depth - stop_depth) / 2) + stop_depth) + 1)
    print(average_depth)
    # breathing
    a = (ata*1*1)
    print(a, 'a')
    b = (((average_depth/33) * (ascent_time - stop_time)*1) + 1)
    print(b, 'b')
    c = (1.5*stop_time)
    print(c, 'c')
    d = (1*1)
    print(d, 'd')
    scr = ((a+b+c+d) * 2)
    print(scr)
    RB = ((scr/ts) * tp)
    print(RB, 'psi')
    if yes_no('Do you want to do another? '):
        break
print("done")
