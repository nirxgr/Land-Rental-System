#Importing writing, operations, and read files in main.
import write
import operations
import read

#Initializing loop=True to run a loop.
loop=True
while loop==True:
    #Displaying welcome message from write file.
    write.WelcomeMessage()
    print('\n')
    # Displaying options for the user from write file.
    write.options()
    # Getting user's choice from operations file.
    user_option=operations.OptionChosen()
    
    if user_option==1:
        # Viewing land details from operations file.
        operations.view_land()
        x= input("<<<Press enter to go back>>>")
        
    elif user_option==2:
        # Renting land.
        write.land_rent()
        write.rentExit() #Exiting land renting process.
        #Exiting the loop.
        loop=False
        
    elif user_option==3:
        #Returning land
        write.land_return() 
        write.returnExit() #Exiting land return process.
        #Exiting the loop.
        loop=False
        
    elif user_option==4:
        #Terminating the program directly.
        write.ProgramExit()
        #Exiting the loop.
        loop=False
        
    else:
        #asking the user to choose only from the options given.
        print("\n Please choose correct option from(1-4)!\n")
