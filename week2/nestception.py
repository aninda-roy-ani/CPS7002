look = input( "Where should I look? ")
if look == "in the bedroom":
    bedroom = input("Where in the bedroom should I look? ")
    if bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif look == "in the bathroom":
    bedroom = input("Where in the bathroom should I look? ")
    if bedroom == "in the bathtub":
        print("Found some rubber duck but no battery")
    else:
        print( "Found some wet surface but no battery.")
elif look == "in the lab":
    bedroom = input("Where in the lab should I look? ")
    if bedroom == "on the table":
        print("Found battery")
    else:
        print( "Found some tools but no battery.")
else:
    print( "I do not know where that is but I will keep looking.")