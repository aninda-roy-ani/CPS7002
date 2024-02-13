import week1.display_text as week1_f1
import week1.display_multiple_text as week1_f2

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
      week1_f1()
    elif selected == 2:
      week1_f2()
    else:
      print("Exiting program... Goodbye!")
      break

run()