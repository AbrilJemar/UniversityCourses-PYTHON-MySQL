def ShowMenu():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~~~~~~~~~~~~~')
    print("""Tell me, what do you want to do?  
1) List courses.
2) Add a new course.
3) Edit a course.
4) Delete a course.
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


#lista lo que esta adentro de la table cursos, esta funcion tengo que modificarla para hacerla dinamica
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

    


#funcion para meter el regstro (se guarda en una lista "Course" la cual me devuelve para poder usarla en connection.py)
def DataRegistration(columns):
    print('\nThese are the columns to complete: ' + ", ".join(columns) + '\n')
    NewCourse = []
    for colum in columns:
        regist = input(f'Enter the {colum}: ')
        NewCourse.append(regist)
        
    print('\nThese are the data of the new course: ' + ', '.join(NewCourse))
    return NewCourse





def DataEditCourse():
    print('Algo')



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
    
    print(IdCourse)
    return IdCourse



