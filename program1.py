 
print ("Hi Welcome to your new safe access, to start please input your name\n")

name = input("Enter your name: ")
print ("\nPlease confirm this is your name Y/N: " + name)

valid = {"Y": True, "N": False}

if valid == True:
    print ("\nThank you for confirming.")
else:
    name = input("Please confirm your name: ")
    print ("\nThank you for confirming your name. We now need to set up the rest of your account.")
    DOB = input("\nPlease enter your DOB (DD/MM/YYYY): ")    
    

print ("\nPlease confirm this is your DOB Y/N: " + DOB )

valid = {"Y": True, "N": False}

if valid == True:
    print ("\nThank you for confirming.")
else:
    DOB = input("\nPlease confirm your DOB: ")

print("\nThank you for confirming your DOB. Now we are able to set your pin ")
pin = input ("\nPlease input your pin: ")

if len(pin) == 4:
    print ("Your Pin is: " + pin)

    print("\nThank you for entering a valid PIN, this will be your unique PIN to access the safe") 
else:
    pin = input("That was not a 4 digit PIN, please try again: ")
    print("\nYour PIN is:" + pin)
    
print("Thank you for confirming your information, we are now able to naviate to the home screen to explore your options\n")

print("You will now be navigated to the menu")
print("Welcome to the menu, please confirm from one of the options below:")
print("1: Change Name")
print("2: Change your DOB")
print("3: Change your personal PIN")
print("4: Quit\n")

option = input("")

if option == "1":
    print("You have selected to change your name.")
    name = input("Please enter your new mame")
    print ("Please confirm this is your name Y/N: " + name)
    valid = {"Y": True, "N": False}
    if valid == True:
        print ("Thank you for confirming.")
    else:
        name = input("Please confirm your name: ")
elif option == "2":
    print("Your have selected to change your DOB")
    DOB = input("Please enter your DOB (DD/MM/YYYY): ")    
    print ("Please confirm this is your DOB Y/N: " + DOB)
    valid = {"Y": True, "N": False}
    if valid == True:
        print ("Thank you for confirming.")
    else:
        DOB = input("Please confirm your DOB: ")
elif option == "3":
    print("You have selected to change your PIN")
    input("Please enteer your current PIN: ")
    if input() == pin:
        pin = input("Please enter your new PIN: ")
        
    if len(pin) == 4:
        print ("Your Pin is: " + pin)
        print("Thank you for entering a valid PIN, this will be your unique PIN to access the safe") 
    else:
        pin = input("That was not a 4 digit PIN, please try again: ")
        print("Your PIN is:" + pin)
elif option == "4":
    print("You have selected to Quit, thank you for your time")

 