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



#Function to print the saved courses on the screen, taking the list "columns" and the tuple "courses" (without the id auto_increment)
def ListCourses(courses, columns):
    print('\nTHESE ARE THE REGISTERED COURSES::')
    counter = 0
    
    print('\033[1m''\n========================================================== ''\033[0m')
    for course in courses:
        counter = counter + 1
        coun = 0
        print(f'\033[1m''COURSE NUMBER ' + str(counter) + '\033[0m')
        for cours in course:
            if isinstance(cours, str):
                data = ("◦ " + columns[coun] + ": " + str(cours))
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
def IdEditCourse(courses, columns):
    print('\nTHESE ARE THE REGISTERED COURSES:')
    counter = 0

    #The courses are listed for the user can see and choose them
    print('\033[1m''\n========================================================== ''\033[0m')
    for course in courses:
        counter = counter + 1
        coun = 0
        print(f'\033[1m''COURSE NUMBER ' + str(counter) + '\033[0m')
        for cours in course:
            if isinstance(cours, str):
                data = ("◦ " + columns[coun] + ": " + str(cours))
                print(data)
                coun = coun + 1

        print('\033[1m''\n\r========================================================== ''\033[0m')
    
    #User is prompted to choose a course
    NumberCourse = input(f'''\nEnter the number of the course you want to edit (from 1 to {counter}): ''')
    NumberCourse = check_user_input(NumberCourse)
    
    num = counter + 1
    while(isinstance(NumberCourse, str) or NumberCourse not in range(1, num)):
        NumberCourse = input("Invalid option. Try again: ")
        NumberCourse = check_user_input(NumberCourse)

    #With the number of the course that was chosen, the course id is saved
    count = 0
    for course in courses:
        count = count + 1
        if count == NumberCourse:
            Id = course[0]
            break

    return Id



#User is prompted to choose a column number to edit
def OptionEditCourse(columns):
    print('\033[1m''\nWhich column do you want to edit?''\033[0m')
    counter = 1
    for column in columns:
        data = ('\033[1m' + str(counter) + '\033[0m' + ". " + column)
        print(data)
        counter = counter + 1
    print('\033[1m' + str(counter) + '\033[0m' + ". all columns")
        
    
    NumberColumn = input(f'\nPlease from 1 to {counter}: ')
    NumberColumn = check_user_input(NumberColumn)
    
    num = counter + 1
    while(isinstance(NumberColumn, str) or NumberColumn not in range(1, num)):
        NumberColumn = input("Invalid option. Try again: ")
        NumberColumn = check_user_input(NumberColumn)

    return NumberColumn
    

    
##User is prompted to enter the new value or values of the choose course
def DataEditCourse(columns, NumberColumn):
    ListColumns = len(columns) + 1

    if NumberColumn == ListColumns:
        #if the user choose edit all columns, the new values are saved on "NewInformation" list
        NewInformation = []
        print('')
        for i in range(len(columns)):
            regist = input(f'Enter the new {columns[i]}: ')
            NewInformation.append(regist)       
        
    else:
        #if the user choose edit one column, the new value is saved on "NewInformation" variable
        count = 0
        for column in columns:
            count = count + 1
            if count == NumberColumn:
                NewInformation = input(f'Enter the new {column}: ')
                break

    return NewInformation
    
    
    



#Function to ask the user which course he wants to remove
def DataDeleteCourse(courses, columns):
    print('\nTHESE ARE THE REGISTERED COURSES:')
    counter = 0
    
    #The courses are listed so that the user can see and choose them
    print('\033[1m''\n========================================================== ''\033[0m')
    for course in courses:
        counter = counter + 1
        coun = 0
        print(f'\033[1m''COURSE NUMBER ' + str(counter) + '\033[0m')
        for cours in course:
            if isinstance(cours, str):
                data = ("◦ " + columns[coun] + ": " + str(cours))
                print(data)
                coun = coun + 1
            

        print('\033[1m''\n\r========================================================== ''\033[0m')
    
    NumberCourse = input(f'Enter the number of the course you want to delete (from 1 to {counter}): ')
    NumberCourse = check_user_input(NumberCourse)
    
    num = counter + 1
    while(isinstance(NumberCourse, str) or NumberCourse not in range(1, num)):
        NumberCourse = input("Invalid option. Try again: ")
        NumberCourse = check_user_input(NumberCourse)

    #The id of the course to be deleted is saved in IdCourse
    count = 0
    for course in courses:
        count = count + 1     
        if count == NumberCourse:
            Id = course[0]
            break
    
    return Id



#User is prompted to choose a column for hte search
def SerchingForSomething(columns):
    print('\033[1m''\nWhich column do you want to search for?''\033[0m')
    counter = 0
    for column in columns:
        counter = counter + 1
        data = ('\033[1m' + str(counter) + '\033[0m' + ". " + column)
        print(data)
        
    NumberColumn = input(f'\nPlease from 1 to {counter}: ')
    NumberColumn = check_user_input(NumberColumn)
    
    num = counter + 1
    while(isinstance(NumberColumn, str) or NumberColumn not in range(1, num)):
        NumberColumn = input("Invalid option. Try again: ")
        NumberColumn = check_user_input(NumberColumn)

    #The column that I select is saved in "Column"
    count = 0
    for column in columns:
        count = count + 1
        if count == NumberColumn:
            Column = column
            break
        
    return Column



#the courses found are shown
def PrintingSearch(results, columns):
    print('\033[1m''\nThis are the found courses: ''\033[0m')
    print('\033[1m''========================================================== \n''\033[0m')
    for Result in results: 
        coun = 0
        for result in Result:
            if isinstance(result, str):
                data = ("◦ " + columns[coun] + ": " + str(result))
                print(data)
                coun = coun + 1
            
        
        print('\033[1m''\n==========================================================\n ''\033[0m')

