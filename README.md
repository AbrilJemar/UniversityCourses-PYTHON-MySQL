In this opportunity i created a program for the administration of a database of a university's courses.

"main.py" is the main program and the import of functionalities, as well as the class in charge of the connection to the database from "connection.py" and "functions.py". I decided to split it this way using the "DataAccessObject" programming pattern.

The program lets the user list, add, remore and edit courses in the database. The edition tool can be used to add or delete columns from the "courses" table using dynamic queries to allow for automatic updating of existing functionalities.

Anyone who wants to test my code can generate test data by running all the queries located in "courses.sql" and correcting the line 11 in "connections.py" with your password of your user "root".
