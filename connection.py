import mysql.connector
from mysql.connector import Error

class DataAccessObject():
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


    def addcolumn(self, column, Size):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(f'ALTER TABLE courses ADD COLUMN {column} varchar({Size})')
                print('COLUMN ADDED SUCCESSFULLY!')

            except Error as ex:
                print('Error trying to connect: {0}' .format(ex))


    def dropcolumn(self, column):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(f'ALTER TABLE courses DROP COLUMN {column}')
                print('COLUMN DELETED SUCCESSFULLY!')

            except Error as ex:
                print('Error trying to connect: {0}' .format(ex))




   #funcion para guardar la tupla columnas en una lista para poder moficarla(las tuplas son estaticas, no se pueden eliminar ni editar lo que tengan adentro)
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


    #funcion para obtener una tupla con los cursos que hay en la tabla courses 
    def listCourses(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute('SELECT * FROM courses ORDER BY Course_name ASC')
                results = cursor.fetchall()

                return results

            except Error as ex:
                print('Error trying to connect: {0}'.format(ex))



 
 #funcion para meter la lista que me dio funciones.DataRegistration() y la lista Columns que 
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

