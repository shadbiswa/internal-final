count = []

def item():

    error_mes = "please enter a number"

    valid = False
    while not valid:
      try:
        x: int(input ("Enter the number of items: "))

      except ValueError:
        print(error_mes)

for item in range(x):
    numbers_items.append(input(f'Enter item {number_items + 1}: '))
print(numbers_items)

item()





