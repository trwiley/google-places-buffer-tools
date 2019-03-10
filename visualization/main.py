import pointcreate
import buffer_points
import visualize_groundcover

def intro_text():
    print('''
    ***********************************************************************************************
    ***********************************************************************************************
                                __                 __                                          
    .-----.-----.-----.-----|  .-----.   .-----|  .---.-.----.-----.-----.                  
    |  _  |  _  |  _  |  _  |  |  -__|   |  _  |  |  _  |  __|  -__|__ --|                  
    |___  |_____|_____|___  |__|_____|   |   __|__|___._|____|_____|_____|                  
    |_____|           |_____|            |__|                                               
    __           ___  ___                      __                   __ __                  
    |  |--.--.--.'  _.'  _.-----.----.   .--.--|__.-----.--.--.---.-|  |__.-----.-----.----.
    |  _  |  |  |   _|   _|  -__|   _|   |  |  |  |__ --|  |  |  _  |  |  |-- __|  -__|   _|
    |_____|_____|__| |__| |_____|__|      \___/|__|_____|_____|___._|__|__|_____|_____|__|  
                                                                                            
    ************************************************************************************************
    ************************************************************************************************

    Welcome to the Google Places Buffer Visualizer. This is a simple command-line tool to visualize
    points selected for using the Google Points API to scrape locations in a defined range using 
    ArcGIS Pro. It is meant to assist in the use-case of attempting to grab all of the locations in 
    a defined political boundary (ie: county or city limits).  
    ''')

def menu():
    print('''
    What would you like to do?
    1) Generate points from a CSV file of coordinates
    2) Generate buffers from a feature class of centerpoints
    3) Use the buffers to visualize how much ground is covered by erasing from a political boundary
    E) Exit
    ''')

def quit_menu():
    print('Are you sure? (Y/N)')
    yesno = input()
    if yesno.upper() == 'Y':
        exit()
    elif yesno.upper() == 'N':
        menu()
        choice_loop()
    else:
        print('Invalid choice!')
        quit_menu()

def choice_loop():
    while True:
        user_input = input()
        if user_input == '1':
            pointcreate.menu()
        elif user_input == '2':
            buffer_points.menu()
        elif user_input == '3':
            visualize_groundcover.menu()
        elif user_input.upper() == 'E':
            quit_menu()
        else:
            print('Invalid choice!')
        menu()

        

def main():
    intro_text()
    menu()
    choice_loop()

main()