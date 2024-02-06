import random

n = int(input("How many live electric cables must I avoid?"))

count = 0

while True:
    is_live_cable = random.choice([True, False])
    if is_live_cable == False :
        print("Found dead electric cable.")
    else:
        count += 1
        print("avoided the live electric cable")

    if count == n:
        break

print("Finished avoiding live cables.")