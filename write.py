#Importing read, operations files in write.
import operations
import read

def WelcomeMessage():
    '''  It prints the welcome message    '''
    # Printing a line of underscores for formatting
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\t\tTechno Property Nepal\n")
    print("\t\t\t\t\t\tKapan, Kathmandu | Phone no: 9813909088")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")


def options():
    ''' It prints the options for user '''
    #Printing different options for the user ro choose
    print("1. View Land For Rent\n")
    print("2. Purchase Available Land For Rent\n")
    print("3. Return Land\n")
    print("4. Exit")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

def ProgramExit():
    ''' It prints thankyou message after exiting the program'''
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\tThank you for Visiting !!")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

def rentExit():
    ''' It prints thankyou message after renting land'''
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\tThank you for renting !!")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

def returnExit():
    ''' It prints thankyou message after returning land'''
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\tThank you for returning !!")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")


def land_rent():
    '''  This function handles the process of renting land and generates the bill   '''
    # Initialize an empty list to store details of rented lands
    rented_details = []
    # Read the land dictionary from the read file and keep in land
    land = read.land_dict()
    # Get the list of kitta numbers from the dictionary
    number = list(land.keys())
    # Get customer information
    name,address,phone = operations.customer_info()
    # To continue the rental process until the user decides to stop
    loop_continuation = True
    while loop_continuation==True:
        # Display the list of available lands
        operations.view_land()
        # Loop until a valid kitta number is entered
        loop = True
        while loop == True:
            # Get the kitta number input from the user
            kitta_num = operations.land_kitta_num_input()
            #checking whether the kitta num is valid or not
            while kitta_num not in number:
                print("Invalid Kitta Number!")
                kitta_num = operations.land_kitta_num_input()
            # Check if the land is available for rent
            availability = land[kitta_num][4]
            if availability=="Not Available":
                print("The land is not available to rent currently.")
            else:
                loop=False
        # Get the anna input from the user and check if it is equal to the total anna of the land
        total_anna=int(land[kitta_num][2])
        loop3=True
        while loop3==True:
            anna=operations.anna_input()
            if anna != total_anna:
                print("The anna you provided is not equals to the anna of this land. Please provide correct anna.")
            else:
                loop3=False
        # Get the number of months to rent the land
        land_month=operations.land_duration_input()
        # Calculate the total rent amount
        total = int(land[kitta_num][3])*land_month
        # Add the details of the rented land to the list
        rented_land = land[kitta_num]
        rented = [kitta_num,rented_land[0],rented_land[1],rented_land[2],rented_land[3],land_month,total]
        rented_details.append(rented)
        # Mark the land as not available for rent
        rented_land[4]="Not Available"
        # Write the updated land dictionary to the file
        file = open("land.txt","w")
        for key,value in land.items():
            file.write(key+","+value[0]+","+value[1]+","+value[2]+","+value[3]+","+value[4])
            file.write("\n")
        file.close()
        # Ask the user if they want to rent more lands
        ans = read.ask_more()
        if ans=="no":
            loop_continuation=False
    # Initialize the grand total variable
    grand_total=0
    # Iterate over each sublist in the rented_details list
    for sublist in rented_details:
        #Add the last element of each sublist (the total rent) to the grand total
        grand_total += sublist[-1]
        
    #Printing Bills
    #importing current datetime 
    import datetime
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    day_time = str(year)+"-"+str(month)+"-"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)
    unique = str(hour)+str(minute)+str(second)
    txtfilename=unique+"_"+name+"_"+"rent"+".txt"
    #printing the bill 
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\tTechno Property Nepal\n")
    print("\t\t\t\t\tKapan, Kathmandu | Phone no: 9813909088\n")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("Bill Number: "+unique+"\n")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("Name of Customer: "+name+"\n")
    print("Address: "+address+"\n")
    print("Phone Number: "+str(phone)+"\n")
    print("Date and time of purchase: "+day_time+"\n")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("Purchase Details: ")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("Kitta No.\t\t City \t\t Direction\t\t Anna  \t\tPrice per month \t Month\t\tTotal\n")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    #to print the bill

    for row in rented_details:
        # Iterate over each element in the row
        for element in row:
            # Print each element, with tab-separated at the end
            print(str(element), end='\t\t')
        # Move to the next line after printing each row
        print()
    # Print a line of underscores for formatting
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    # Print the grand total
    print("Grand Total: Rs.",grand_total,"\n")

    #creating a new .txt bill with unique bill number
    #opening a new textfile in write mode
    file = open(txtfilename,"w")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTechno Property Nepal\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tKapan, Kathmandu | Phone no: 9813909088\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("Bill Number: "+unique+"\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("Name of Customer: "+name+"\n")
    file.write("Address: "+address+"\n")
    file.write("Phone Number: "+str(phone)+"\n")
    file.write("Date and time of purchase: "+day_time+"\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("Purchase Details: ")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("Kitta No.\t\t City \t\t Direction\t\t Anna  \tPrice per month \tMonth\tTotal\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")


    for rows in rented_details:
        #initializing index as 0
        index = 0
        # Iterate over each items in the rows
        for items in rows:
             # Writing each items, with tab at the end
            file.write(str(items)+"\t\t")
            #using if to add an extra tab at index 4
            if index == 4:
                #adding an extra tab
                file.write("\t")
            #adding index by 1 after every loop
            index += 1
        #changing the line
        file.write("\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    # Writing the grand total
    file.write("Grand Total: Rs."+str(grand_total)+"\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    #closing the file
    file.close()


def land_return():
    '''  This function handles the process of renting land and generates the bill   '''
    # List to store details of returned land
    return_land_details = []
    # Retrieving land details from the read file
    land = read.land_dict()
    # Extracting land keys
    number = list(land.keys())
    # Getting customer information
    name,address,phone = operations.customer_info()
    # To continue the return process until the user decides to stop
    loop_continuation = True
    while loop_continuation==True:
        # Displaying available land for return 
        operations.view_land()
        loop = True
        while loop == True:
            # Getting kitta number of the land to be returned
            kitta_num = operations.land_kitta_num_input()
            #checking whether the kitta num is valid or not
            while kitta_num not in number:
                print("Invalid Kitta Number!")
                kitta_num = operations.land_kitta_num_input()
            availability = land[kitta_num][4]
            # Checking if the land is available for return
            if availability=="Available":
                print("Please Check Kitta number! This is not the land you are trying to return as it is already available for rent!")
            else:
                loop=False

        # Getting rent month and return month
        rent_month=operations.land_rent_input()
        return_month=operations.land_return_input()
        '''
        Checking whether the land is returned late or not
        If returned late, calculating the fine as 10% per month of total and adding it in the total calculated before fine
        else keeping the fine 0
        '''
        if return_month>rent_month:
            print("Since you returned the land late, a fine will also be charged!")
            fine_number_of_month=return_month-rent_month
            fine_month=0.10*fine_number_of_month
            total_before_fine = int(land[kitta_num][3])*rent_month
            fine = int(total_before_fine*fine_month)
            total = total_before_fine+fine
        else:
            fine=0
            total = int(land[kitta_num][3])*rent_month
        return_land = land[kitta_num]
        rented = [kitta_num,return_land[0],return_land[1],return_land[2],return_land[3],rent_month,str(fine),total]
        return_land_details.append(rented)
        # Changing availability status of the returned land to "Available"
        return_land[4]="Available"
        # Updating land details in the file
        file = open("land.txt","w")
        for key,value in land.items():
            file.write(key+","+value[0]+","+value[1]+","+value[2]+","+value[3]+","+value[4])
            file.write("\n")
        file.close()
        # Asking user if there are more lands to return
        ans = read.return_more()
        if ans=="no":
            loop_continuation=False
    # Calculating grand total of return
    grand_total=0
    for sublist in return_land_details:
        grand_total += sublist[-1]
    #Printing Bills
    import datetime
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    day_time = str(year)+"-"+str(month)+"-"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second)
    unique = str(hour)+str(minute)+str(second)
    txtfilename=unique+"_"+name+"_"+"return"+".txt"
    #printing the bill
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\tTechno Property Nepal\n")
    print("\t\t\t\t\tKapan, Kathmandu | Phone no: 9813909088\n")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("Bill Number: "+unique+"\n")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("Name of Customer: "+name+"\n")
    print("Address: "+address+"\n")
    print("Phone Number: "+str(phone)+"\n")
    print("Date and time of purchase: "+day_time+"\n")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("Purchase Details: ")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    print("Kitta No.\t\t City \t\t Direction\t\t Anna  \t\tPrice per month \t Month\t\tFine\t\tTotal\n")
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")

    for row in return_land_details:
    # Iterate over each element in the row
        for element in row:
            # Print the element
            print(str(element), end= '\t\t')
        # Move to the next line after printing each row
        print()
  
    print("____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    # Print the grand total
    print("Grand Total: Rs.",grand_total,"\n")

    #creating a new .txt bill with unique bill number
    file = open(txtfilename,"w")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTechno Property Nepal\n")
    file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tKapan, Kathmandu | Phone no: 9813909088\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("Bill Number: "+unique+"\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("Name of Customer: "+name+"\n")
    file.write("Address: "+address+"\n")
    file.write("Phone Number: "+str(phone)+"\n")
    file.write("Date and time of purchase: "+day_time+"\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("Purchase Details: ")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    file.write("Kitta No.\t\t City \t\t Direction\t\t Anna  \tPrice per month \tMonth\t Fine\t\tTotal\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")

    # Iterate over each row in return_land_details and write the details to the file
    for row in return_land_details:
        #initializing index as 0
        index = 0
        #iterate over each element in the row
        for element in row:
            # Writing each items, with tab at the end
            file.write(str(element)+ "\t\t")
            #using if to add an extra tab at index 4
            if index == 4:
                #adding an extra tab
                file.write("\t")
            #adding index by 1 after every loop
            index += 1
        #changing the line
        file.write("\n")
        
    # Print a line of underscores for formatting
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    # Print the grand total to the file
    file.write("Grand Total: Rs."+str(grand_total)+"\n")
    file.write("________________________________________________________________________________________________________________________________________________________\n")
    #closing the file
    file.close()
        
        
        
        

