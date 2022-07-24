while True:
    try:
        number_item = int(input('Enter the number of items: '))
        break
    except ValueError:
        print('You must enter a number')

item = []
separator = ", "
for items in range(number_item):
    item.append(input('Enter item: '))
print("Your items are:", separator.join(item))




