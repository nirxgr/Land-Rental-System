#Importing read, write files in operations.
import read
import write

def OptionChosen():
    ''' It takes the option from user, validates it and returns.   '''
    #running a while loop until valid input is received.
    while True:
        #Using try except to handle exceptions.
        try:
            #Asking user for input.
            chosen = int(input("What kind of service are you interested in?\nPlease choose an option: "))
            # checking if the user given number lies in 1 to 4 or not
            if chosen not in [1,2,3,4]:
                print("Invalid option. Please choose a valid option (1, 2, 3, or 4)!")
            else:
                #Breaking out of loop
                break
        except ValueError:
            print("Please enter a valid integer.")
    #Returning user's choice.
    return chosen

def customer_info():
    ''' It takes user informations checks it and returns.  '''
    #running a while loop until valid input is received.
    while True:
        #Asking user for input.
        name = input("Enter your name : ")
        if(len(name)>0):
            #Breaking out of loop
            break
        else:
            print("Error!Please provide your name!")
    #running a while loop until valid input is received.
    while True:
        address = input("Enter your address : ")
        if(len(address)>0):
            #Breaking out of loop
            break
        else:
            print("Error!Please provide your address!")
    loop=True
    #running a while loop until valid input is received.
    while loop==True:
        try:
            phone = int(input("Enter your phone number : "))
            #checking if the length of phone number is equals to 10 or not
            if len(str(phone))!=10:
                print("Please give your phone number correctly!")
            else:
                #setting loop equals to false to break out of loop
                loop=False
        except ValueError:
            print("Please give your phone number correctly!")
    #Returning user's choice.
    return name,address,phone

def land_kitta_num_input():
    ''' It takes the kitta number from user, validates it and returns.   '''
    kitta_num = input("Enter kitta number: ")
    #Returning user's choice.
    return kitta_num


def anna_input():
    ''' It takes anna from user, validates it and returns.   '''
    while True:
        try:
            anna=int(input("Enter the anna you want to rent: "))
            #Breaking out of loop
            break
        except ValueError:
            print("Please enter an integer!")
    #Returning user's choice.
    return anna
            
def land_duration_input():
    ''' It takes the number of months user would like to rent the land for, validates it and returns.   '''
    #asking user the number of months they would like to rent the land for.
    while True:
        #Using try except to handle exceptions.
        try:
            month=int(input("Enter the number of months you would like to rent the land: "))
            '''not letting the user to  enter the month below 1
            checking whether the user provided month is valid or not.'''
            if month<1:
                print("Please enter the number of months correctly!")
            else:
                break
        except ValueError:
            print("Please enter an integer!")
    #Returning user's choice.
    return month
            

def land_rent_input():
    ''' It takes the land rent month from user, validates it and returns   '''
    while True:
        #Using try except to handle exceptions.
        try:
            rent_month=int(input("Enter the number of months you rented the land for: "))
            '''not letting the user to  enter the month below 1
            checking whether the user provided month is valid or not.'''
            if rent_month<1:
                print("Please enter the number of months correctly!")
            else:
                #Breaking out of loop
                break
        except ValueError:
            print("Please enter an integer!")
    #Returning user's choice.
    return rent_month
        

 
        
def land_return_input():
    ''' It takes the land return month from user, validates it and returns   '''
    while True:
        #Using try except to handle exceptions.
        try:
            return_month=int(input("How many months have passed since the day you rented it?: "))
            '''not letting the user to  enter the month below 1
            checking whether the user provided month is valid or not.'''
            if return_month<1:
                print("Please enter the number of months correctly!")
            else:
                #Breaking out of loop
                break
        except ValueError:
            #printing error message
            print("Please enter an integer!")
    #Returning user's choice.
    return return_month   
        

def view_land():
    ''' It displays the stocks of the land with all of its details. '''
    #printing welcome message
    write.WelcomeMessage()
    print("Kitta No.\t\t City \t\t Direction\t\t Anna  \t\t Price \t\t Availability")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    #calling a function from read file and storing it in d
    d = read.land_dict()
    for key,value in d.items():
        print (key,end="\t\t") # ending with double tab after printing a key. 
        for v in value:
            print(v,end="\t\t")# ending with double tab after printing a key.
        #changing the line.
        print("\n")




