x = input("Please enter a marker: ")
s = input("Please enter a sequence: ")
count = 0
fi = 0
li = 0
for i in range(len(s)):
    if s[i] == x:
        if count == 0:
            fi = i
        li = i
        count += 1

print("The distance between the markers is: ", li-fi-count+1)