

def escape(plan="go deeper"):
    if plan == "jump over":
        print("We cannot escape that way! The boulder is too big!" )
    elif plan == "run around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("Going deeper might just work!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

escape("jump over")
escape(plan="run around")
escape("go deeper")
escape()
