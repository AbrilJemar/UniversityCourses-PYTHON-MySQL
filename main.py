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
            
            ################################## List courses #######################################
            case 1:
                Courses = DAO.listCourses()
                
                if len(Courses) > 0:
                    Columns = DAO.listColumns()
                    functions.ListCourses(Courses, Columns)

                else:
                    Exit = functions.GoBack()
                    if Exit == 2:
                        print('Thanks for using this program')
                        break  
                

                
                
            ################################## Add a course #######################################
            case 2:
                Columns = DAO.listColumns()
                NewCourse = functions.DataRegistration(Columns)
                DAO.addCourse(NewCourse, Columns)    


                

            ################################## Edit a course ######################################
            case 3:
                try:
                     #it's not ready yet
                except:
                    print('ERROR')


                    

            ################################## Remove a course ####################################
            case 4:
                try:
                    courses = DAO.listCourses()
                    if len(courses) > 0:
                        sure = functions.SureDelete()
                        if sure == 1:
                            columns = DAO.listColumns()
                            IdCourse = functions.DataDeleteCourse(courses, columns)
                            DAO.deleteCourse(IdCourse)

                    else:
                        Exit = functions.GoBack()
                        if Exit == 2:
                            print('Thanks for using this program')
                            break
                            
                except:
                    print('ERROR')

                    


            ################################## Search a course ###################################
            case 5:
                try:
                    #it's not ready yet
                except:
                    print('ERROR')

 


            ################################## Modify columns ####################################
            case 6:
                while True:
                    action = functions.Modify()
                    match action:
                        case 1:
                            Column = input('Enter the name for the new column: ')
                            DAO.addcolumn(Column)

                        case 2:
                            Column = input('Which column are you going to delete?: ')
                            DAO.dropcolumn(Column)

                        case 3:
                            break


                            
                            
            ################################## Close program #####################################
            case 7: 
                print('\r\n \n \n~~~~~~~~~~~    OFF    ~~~~~~~~~~~~')
                break


App()

