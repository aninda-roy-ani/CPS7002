n = int(input("How many bars should be charged?"))

nBars = 0

while nBars < n:
    print("Charging:", end="")
    nBars += 1
    i = 0
    while i<nBars:
        i += 1
        print(" █", end="")
    print()

print("The battery is fully charged")