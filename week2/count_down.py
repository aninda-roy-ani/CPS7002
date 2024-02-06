n = int(input("How far are we from the cave?: "))

nChanged = 0

for i in range(n,0,-1):
    if i == 1:
        print(i,"step remaining")
    else:
        print(i,"steps remaining")