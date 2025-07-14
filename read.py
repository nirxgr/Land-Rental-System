def land_dict():
    '''It creates a dictionary containing land details from a file which returns land_details which contains land details.'''

    #Creating a dictionary to store land details.
    land_details = {}
    #Opening file for reading.
    file = open("land.txt", "r")
    #Reading lines from file.
    lines = file.readlines()
    #using a for loop
    for line in lines:
        line = line.replace("\n", "").split(",") # Splitting lines by comma.
        key = line[0] #Extracting key.
        value=[]
        for i in range(1, len(line)):
            value.append(line[i].strip()) #Stripping whitespace and adding values.
        # Adding key-value pair to dictionary.
        land_details[key] = value
    #Closing the file.
    file.close()
    return land_details


def ask_more():
    '''It asks user if they wish to buy more land or not and returns user choice in yes or no.'''
    #running a while loop until valid input is received.
    while True:
        try:
            #Asking user for input.
            ask = input("Do you wish to buy more land? (yes/no):")
            if ask.lower() not in['yes','no']:
                #Raising error for invalid input.
                raise ValueError("Invalid Choice. Please enter ' yes' or 'no' ")
            else:
                #Breaking out of loop
                break
        except ValueError as error:
            print(error) #Displaying error message.
    #Returning user's choice.
    return ask

def return_more():
    '''It asks user if they wish to return more land or not and returns user choice in yes or no.'''
    while True:
        try:
            #Asking user for input.
            ask = input("Do you want to return more land? (yes/no):")
            if ask.lower() not in['yes','no']:
                # Raising error for invalid input.
                raise ValueError("Invalid Choice. Please enter ' yes' or 'no' ")
            else:
                #Breaking out of loop
                break
        except ValueError as error:
            print(error) #Displaying error message.
    #Returning user's choice.
    return ask
                

