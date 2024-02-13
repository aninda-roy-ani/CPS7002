

def display_ladder(steps):
    asciii = '''
    | |
    ***'''
    print(asciii*steps)

def create_ladder():
    inp = int(input("Enter the steps: "))
    display_ladder(inp)

create_ladder()