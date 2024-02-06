import random

print("Menu: ")
print("[1] Random number \n[2] Random word")
inp = input("Please enter your selection: ")

if not inp.isdigit():
    print("Wrong input")
else:
    if inp == "1":
        print("Random number is: ",random.randint(1,100))
    elif inp == "2":
        print("Random word is: ", random.choice(["gsdv","hasbd","ajshgd"]))
    else:
        print("Enter between 1 and 2")
