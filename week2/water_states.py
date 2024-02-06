temp = int(input("Enter the temperature: "))

state = ""

if (temp <= 0):
    state = "solid"
elif (temp >= 100):
    state = "gas"
else:
    state = "liquid"

print("current state is: "+state)

if (state == "liquid"):
    print("the water is consumable")
else:
    print("the water is not consumable")