def ShowMenu():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~~~~~~~~~~~~~')
    print("""Tell me, what do you want to do?  
1) List courses.
2) Add a new course.
3) Edit a course.
4) Remove a course.
5) Search for a course.
6) Modify a column.
7) Exit.
    """)
        


# Function to convert the "input" into numbers
def check_user_input(x):
    try:
        # Convert it into integer
        val = int(x)
    except ValueError:
        try:
            # Convert it into float
            val = float(x)
        except ValueError:
            val = x

    return (val)



#Function for go back to main menu
def GoBack():
    Exit = input('''\nNo courses found. Go back to main menu?
1) YES.
2) NO.

Choose an option: ''')
    Exit = check_user_input(Exit)
        
    while(isinstance(Exit, str) or Exit not in [1,2]):
        Exit = input("Invalid option. Try again: ")
        Exit = check_user_input(Exit)    
    
    return Exit



#Function to ask if the user is sure that he wants to remove a course
def SureDelete():
    sure = input('''Are you sure you want to remove a course?
1) YES.
2) NO.

Choose an option: ''')
    sure = check_user_input(sure)
    while(isinstance(sure, str) or sure not in [1,2]):
        sure = input("Invalid option. Try again: ")
        sure = check_user_input(sure)    
    
    return sure



#Function to ask what action the user wants to perform when modifying columns
def Modify():
    action = input('''\nWhat do you want to modify?:
1) Add a new column.
2) Delete a column.
3) Go back to main menu.                          

''')

    action = check_user_input(action)
    while(isinstance(action, str) or action not in [1,2,3]):
        action = input("Invalid option. Try again: ")
        action = check_user_input(action) 
    
    return action



#Function to print the saved courses on the screen, taking the list "columns" and the tuple "courses"
def ListCourses(courses, columns):
    print('\nTHESE ARE THE REGISTERED COURSES::')
    counter = 0
    
    print('\033[1m''\n========================================================== ''\033[0m')
    for cour in courses:
        counter = counter + 1
        coun = 0
        print(f'\033[1m''COURSE NUMBER ' + str(counter) + '\033[0m')
        for cou in cour:
            
            data = ("◦ " + columns[coun] + ": " + str(cou))
            print(data)
            coun = coun + 1

        print('\033[1m''\n\r========================================================== ''\033[0m')



#Function save the information of a new course in the "NewCourse" list, to use it in "connection.py"
def DataRegistration(columns):
    print('\nThese are the columns to complete: ' + ", ".join(columns) + '\n')
    NewCourse = []
    for colum in columns:
        regist = input(f'Enter the {colum}: ')
        NewCourse.append(regist)
        
    print('\nThese are the data of the new course: ' + ', '.join(NewCourse))
    return NewCourse



#Function to ask the user which course he wants to edit
def DataEditCourse():
    print('something')



#Function to ask the user which course he wants to remove
def DataDeleteCourse(courses, columns):
    print('\nTHESE ARE THE REGISTERED COURSES:')
    counter = 0
    
    print('\033[1m''\n========================================================== ''\033[0m')
    for cour in courses:
        counter = counter + 1
        coun = 0
        print(f'\033[1m''COURSE NUMBER ' + str(counter) + '\033[0m')
        for cou in cour:
            
            data = ("◦ " + columns[coun] + ": " + str(cou))
            print(data)
            coun = coun + 1

        print('\033[1m''\n\r========================================================== ''\033[0m')
    
    NumberCourse = input(f'''Enter the number of the course you want to delete (from 1 to {counter}): ''')
    NumberCourse = check_user_input(NumberCourse)
    
    num = counter + 1
    while(isinstance(NumberCourse, str) or NumberCourse not in range(1, num)):
        NumberCourse = input("Invalid option. Try again: ")
        NumberCourse = check_user_input(NumberCourse)

    count = 0
    for cour in courses:
        count = count + 1
            
        if count == NumberCourse:
            IdCourse = cour[0]
            break
    
    return IdCourse



