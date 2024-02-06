triangle = input("What type of triangle do we have?: ")

if (triangle == "scalene"):
    print("All sides are different")
    yn = input("Do you wish to see a famous scalene triangle?: ")
    if(yn.lower() == "yes"):
        print("Famous scalene triangle: 3, 4, 5")
elif (triangle == "equilateral"):
    print("all sides are equal")
else:
    print("Two sides are the same")