try:
    age=int(input("enter your budget: "))
except:
   print("This is not a vaild number")



while True:
        choice=int(input("enter a whole number or a decimal number. "))
        if choice > 5 or choice < 1:
            print("not a vaild choice -try again")
        else:
            print("choice is", choice)
            break
