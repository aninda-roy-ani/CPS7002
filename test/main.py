import display_text
import display_multiple_text


def menu():
  print("""What would you like to do?
  Week 1:
  [1] Display Text
  [2] Display Multiple Text

  Other:
  [0] Exit""")

  selected = int(input("Enter selected option: "))
  return selected

def run():
  while(True):
    selected = menu()

    if selected == 1:
      display_text.dis()
    elif selected == 2:
      display_multiple_text.dis2()
    else:
      print("Exiting program... Goodbye!")
      break

run()



