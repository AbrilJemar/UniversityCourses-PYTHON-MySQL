from connection import DataAccessObject
import functions

#Administration of university courses application
def App():
    DAO = DataAccessObject()

    while True:
        functions.ShowMenu()
        option = input("Choose an option: ")
        option = functions.check_user_input(option)
        
        while(isinstance(option, str) or option not in [1,2,3,4,5,6,7]):
            option = input("Invalid option. Try again: ")
            option = functions.check_user_input(option)    
        
        match option:
            
            case 1:
                Courses = DAO.listCourses()
                
                
                if len(Courses) > 0:

                    Columns = DAO.listColumns()
                    functions.ListCourses(Courses, Columns)

                else:
                    Exit = input('''\nNo course found. Go back to main menu?
1) YES
2) NO

Choose an option: ''')
                    Exit = functions.check_user_input(Exit)
        
                    while(isinstance(Exit, str) or Exit not in [1,2]):
                        Exit = input("Invalid option. Try again: ")
                        Exit = functions.check_user_input(Exit)    

                    if Exit == 2:
                        print('Thanks for using this program')
                        break

                

        
            case 2:
                
                Columns = DAO.listColumns()
                NewCourse = functions.DataRegistration(Columns)
                DAO.addCourse(NewCourse, Columns)    



                
            case 3:
                try:
                    DAO.EditCourse(NewCourse)    


                except:
                    print('ERROR')





            case 4:
                try:
                    courses = DAO.listCourses()
                    if len(courses) > 0:
                        sure = input('''Are you sure you want to delete a course?
1) YES.
2) NO.

Choose an option: ''')
                        sure = functions.check_user_input(sure)
                        while(isinstance(sure, str) or sure not in [1,2]):
                            sure = input("Invalid option. Try again: ")
                            sure = functions.check_user_input(sure)    

                        if sure == 1:
                            columns = DAO.listColumns()
                            IdCourse = functions.DataDeleteCourse(courses, columns)
                            DAO.deleteCourse(IdCourse)

                        
                    else:
                        Exit = input('''\nNo courses to drop. Go back to main menu?
1) YES.
2) NO.

Choose an option: ''')
                        Exit = functions.check_user_input(Exit)
        
                        while(isinstance(Exit, str) or Exit not in [1,2]):
                            Exit = input("Invalid option. Try again: ")
                            Exit = functions.check_user_input(Exit)    

                        if Exit == 2:
                            print('Thanks for using this program')
                            break



                except:
                    print('ERROR')




            case 5:
                try:
                    '''Columns = DAO.listColumns()
                    functions.ListColumns(Columns)'''
                      


                except:
                    print('ERROR')


            case 6:
                while True:
                    action = input('''\nWhat do you want to modify?:
1) Add a new column.
2) Delete a column.
3) Go back to main menu.                          

''')

                    action = functions.check_user_input(action)
                    while(isinstance(action, str) or action not in [1,2,3]):
                        action = input("Invalid option. Try again: ")
                        action = functions.check_user_input(action) 

                
                    match action:
                        case 1:
                            Column = input('Enter the name for the new column: ')
                            DAO.addcolumn(Column)

                        case 2:
                            Column = input('Which column are you going to delete?: ')
                            DAO.dropcolumn(Column)

                        case 3:
                            break


            case 7: 
                print('\r\n \n \n~~~~~~~~~~~    OFF    ~~~~~~~~~~~~')
                break














App()
