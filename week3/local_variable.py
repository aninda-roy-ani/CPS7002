
def cross_bridge(steps=5):
    if steps <= 0:
        steps = 0
    elif steps >= 5:
        steps = 5

    for i in range(steps):
        if i == 0:
            print("Taken 1 step")
        else:
            print("Taken",i+1,"steps")

    steps_remaining = 10-steps

    if steps_remaining <= 5:
        print("The bridge is collapsing!")
    else:
        print("We need more to go!")

cross_bridge(steps=3)
cross_bridge(steps=7)