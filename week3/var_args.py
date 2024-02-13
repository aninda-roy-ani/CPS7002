

def climb(*args):
    bop = 0
    beep = 0
    for i in range(len(args)):
        if((i+1)%2 == 0):
            beep += args[i]
        else:
            bop += args[i]
    if(beep>bop):
        print("Beep is closer to top than Bop")
    elif(bop>beep):
        print("Bop is closer to top than Beep")
    else:
        print("Equal")

climb(1, 2, 3, 4)
climb(1, 1, 3, 2)
climb(1, 1, 1, 1)