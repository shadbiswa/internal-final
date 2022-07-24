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


#main routine goes here
budget = int_check("what is your budget?: ")
print("Your budget is ${:.2f}".format(budget))

