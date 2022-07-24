def int_check(question):

  error = ("please enter a number above 0")

  valid = False
  while not valid:

    #ask user for number and check if it valid
      try:
          response = float(input(question))

          if response <= 0:
              print(error)
          else:
              return response

    #if an integer is not entered, display an error
      except ValueError:
        print(error)


budget = int_check("what is your budget?: ")



while True:
    try:
        number_of_words = int(input('Enter the number of words: '))
        break
    except ValueError:
        print('You must enter a number')

words = []
separator = ", "
for word in range(number_of_words):
    words.append(input(f'Enter word {word + 1}: '))
print(separator.join(words))

print("Your budget is ${:.2f}".format(budget))

