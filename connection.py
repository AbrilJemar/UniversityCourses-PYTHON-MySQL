import mysql.connector
from mysql.connector import Error

class DataAccessObject():
    #Connects to the database
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='YourPassword',
                db='university' 
            )
        
        except Error as ex:
            print('Error trying to connect: {0}'.format(ex))



    #Add a column
    def addcolumn(self, column):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(f'ALTER TABLE courses ADD COLUMN {column} varchar(100)')

                print('COLUMN ADDED SUCCESSFULLY!')

            except Error as ex:
                print('Error trying to connect: {0}' .format(ex))



    #Delete a column
    def dropcolumn(self, column):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(f'ALTER TABLE courses DROP COLUMN {column}')

                print('COLUMN DELETED SUCCESSFULLY!')

            except Error as ex:
                print('Error trying to connect: {0}' .format(ex))



   #Takes existing columns and saves them in the "Columns" list
    def listColumns(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(f'''SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = "university" AND TABLE_NAME = "courses" ORDER BY ORDINAL_POSITION''')
                results= cursor.fetchall()
                Columns = []
                for colum in results:
                    separator = " "  
                    chain = separator.join(str(part) for part in colum)
                    Columns.append(chain)
                    
                return Columns
            except Error as ex:
                print('Error trying to connect: {0}' .format(ex))



    #Gets a tuple with the existing courses
    def listCourses(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute('SELECT * FROM courses ORDER BY Course_name ASC')
                results = cursor.fetchall()

                return results

            except Error as ex:
                print('Error trying to connect: {0}'.format(ex))


 
    #Insert the course obtained in functions.DataRegistration() in tha table
    def addCourse(self, NewCourse, columns):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                exe = ('INSERT INTO courses('+", ".join(columns)+') VALUES("'+'", "'.join(NewCourse)+'")')
                cursor.execute(exe)
                self.connection.commit()

                print('\nCOURSE ADDED SUCCESSFULLY! \n')

            except Error as ex:
                print('Error trying to connect: {0}'.format(ex))

                
                
    #Edit the selected course with the data entered            
    def editCourse(self, idcourse, course, columns):
        if self.connection.is_connected():
            try:
                counter = 0
                for i in range(len(columns)):
                    if i != 0:
                        cursor = self.connection.cursor()
                        exe = ('UPDATE courses SET ' + columns[i] + ' = "'  + course[counter] + '" WHERE id_course = "'  + idcourse + '"')
                        cursor.execute(exe)
                        self.connection.commit()
                        counter = counter + 1

                print('\nCOURSE EDITED SUCCESSFULLY! \n')        
                
                print('\033[1m'"THAT'S HOW IT'S SAVED: "'\033[0m')
                cursor.execute('SELECT * FROM courses WHERE id_course = "' + idcourse + '"')
                course = cursor.fetchall()
                coun = 0
                print('\033[1m''========================================================== ''\033[0m')
                for cour in course:
                    for cou in cour:
                        data = ("◦ " + columns[coun] + ": " + str(cou))
                        print(data)
                        coun = coun + 1

                print('\033[1m''========================================================== ''\033[0m')
        
            except Error as ex:
                print('Error trying to connect: {0}'.format(ex))

                

    #Delete the chosen course
    def deleteCourse(self, IdCourse):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                exe = ('DELETE FROM courses WHERE id_course = "{0}"')
                cursor.execute(exe.format(IdCourse))
                self.connection.commit()

                print('\nCOURSE DELETED SUCCESSFULLY! \n')

            except Error as ex:
                print('Error trying to connect: {0}'.format(ex))

