line = input("What phrase do you see: ")
print("Reversing...")
for i in range(len(line),0,-1):
    print(line[i-1], end="")