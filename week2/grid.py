row = int(input("How many rows should I display?: "))
col = int(input("How many columns should I display?: "))

print("Here I go...")

for i in range(row):
    for j in range(col):
        print(f"|🌞|",end="")
    print()
print()
print("Done!")