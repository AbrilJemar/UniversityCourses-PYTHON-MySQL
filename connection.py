import mysql.connector
from mysql.connector import Error

class DataAccessObject():
    #Connects to the database
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='SamueldeLuque777',
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
    def listColumns(self): #Without id autoincrement
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
                
                del Columns[0]
                return Columns
            except Error as ex:
                print('Error trying to connect: {0}' .format(ex))




    #Takes existing columns and saves them in the "Columns" list
    def listColumnsId(self): #with id autoincrement
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
                cursor.execute('SELECT * FROM courses ORDER BY id ASC')
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
    def editCourse(self, id, course, columns):
        if self.connection.is_connected():          #y se hay 2? implementar el id auto increment
            try:
                counter = 0
                for i in range(len(columns)):
                    cursor = self.connection.cursor()
                    print(columns[i])
                    exe = ('UPDATE courses SET ' + columns[i] + ' = "'  + course[counter] + '" WHERE id = '  + str(id) + '')
                    print(exe)
                    cursor.execute(exe)
                    self.connection.commit()
                    counter = counter + 1

                print('\nCOURSE EDITED SUCCESSFULLY! \n')        
                print('\033[1m'"THAT'S HOW IT'S SAVED: "'\033[0m')
                
                cursor.execute('SELECT * FROM courses WHERE id = "' + str(id) + '"')
                course = cursor.fetchall()
                coun = 0
                print('\033[1m''========================================================== ''\033[0m')
                for cours in course:
                    for cour in cours:
                        if isinstance(cour, str):
                            data = ("◦ " + columns[coun] + ": " + str(cour))
                            print(data)
                            coun = coun + 1

                print('\033[1m''========================================================== ''\033[0m')
        
            except Error as ex:
                print('Error trying to connect: {0}'.format(ex))




    #Delete the chosen course
    def deleteCourse(self, Id):
        if self.connection.is_connected(): #y se hay 2? implementar el id auto increment
            try:
                cursor = self.connection.cursor()
                exe = ('DELETE FROM courses WHERE id = {0}')
                cursor.execute(exe.format(Id))
                self.connection.commit()

                print('\nCOURSE DELETED SUCCESSFULLY! \n')

            except Error as ex:
                print('Error trying to connect: {0}'.format(ex))




    def searchCourse(self, Column, Search):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                exe = ('SELECT * FROM courses WHERE ' + Column + ' LIKE "%' + Search + '%"')
                
                cursor.execute(exe)
                results = cursor.fetchall()
                
                return results
            except Error as ex:
                print('Error trying to connect: {0}'.format(ex))