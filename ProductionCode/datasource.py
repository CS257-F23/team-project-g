import psycopg2
from ProductionCode import psqlConfig as config

class DataSource:
    connection = None; 
    def __init__(self):
        '''constructor for DataSource class, establishes connection with database'''
        self.connection = self.connect()

    def connect(self):
        '''establishes connection with database'''
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host = "localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    
    def getAll(self):
        '''return all data that's in the table teamg'''
        #Open a cursor to perform database operations
        cursor = self.connection.cursor()

        #Execute a query
        cursor.execute("SELECT * FROM teamg")

        #Retrieve query results
        records = cursor.fetchall()

        return records
    
    def get_food_allergy(self, food, allergy):
        '''Arguments: A single food and a single allergen
        Purpose: Check if a food contains a specific allergen'''
        try:
            #set up a cursor
            cursor = self.connection.cursor()
            #make the query using %s as a placeholder for the variable
            query = "SELECT * FROM teamg WHERE LOWER(food)=%s AND "+ allergy + " = 1"


            #executing the query and saying that the magnitude variable 
            cursor.execute(query, (food.lower(), ))

            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def get_calorie_from_table(self, food_name):
        '''Retrieve and return the calories of a specified food item.'''
        try:
            #set up a cursor
            cursor = self.connection.cursor()
            #make the query using %s as a placeholder for the variable
            query = "SELECT calories FROM teamg WHERE LOWER(food)=%s"


            #executing the query and saying that the magnitude variable 
            cursor.execute(query, (food_name.lower(), ))

            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def food_exist(self, food_name):
        '''Retrieve and return whether a food exists in the table.'''
        try:
            #set up a cursor
            cursor = self.connection.cursor()
            #make the query using %s as a placeholder for the variable
            query = "SELECT * FROM teamg WHERE LOWER(food)=%s"


            #executing the query and saying that the magnitude variable 
            cursor.execute(query, (food_name.lower(), ))

            if cursor.fetchall() == []:
                return False   
            return True

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

if __name__ == '__main__':
    my_source = DataSource()
    print(my_source.food_exist("mato")) #prints out all rows with calorie less than 300
   