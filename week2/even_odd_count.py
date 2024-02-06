a = int(input("Please enter 1st whole number: "))
b = int(input("Please enter 2nd whole number: "))
c = int(input("Please enter 3rd whole number: "))

count = 0

if b%2 == 0:
    count += 1

if a%2 == 0:
    count += 1

if c%2 == 0:
    count += 1

print("Number of even numbers: ", count)
print("Number of odd numbers: ", 3-count)
