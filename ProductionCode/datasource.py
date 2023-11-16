import psycopg2
import ProductionCode.psqlConfig as config

class DataSource:
    connection = None; 
    def __init__(self):
        '''constructor for DataSource class, establishes connection with database'''
        self.connection = self.connect()

    def connect(self):
        '''Purpose: establishes connection with database
        Returns: the connection'''
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host = "localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    
    def get_food_allergy(self, food, allergy):
        '''Arguments: A single food and a single allergen
        Purpose: Check if a food contains a specific allergen
        Return: tuples of the check result, or None if the food contains no allergy'''
        try:
            cursor = self.connection.cursor()
            query = "SELECT food FROM food_information WHERE LOWER(food)=%s AND "+ allergy + " = True"
            cursor.execute(query, (food.lower(), ))

            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def get_calorie_from_table(self, food_name):
        '''Arguments: A single food and a single allergen
        Purpose: Retrieve and return the calories of a specified food item.
        Returns: a tuple of a calories result, or None when there is a problem in execution'''
        try:
            cursor = self.connection.cursor()
            query = "SELECT calories FROM food_information WHERE LOWER(food)=%s"
            cursor.execute(query, (food_name.lower(), ))

            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def food_exist(self, food_name):
        '''Arguments: A single food and a single allergen
        Purpose: Retrieve and return whether a food exists in the table.
        Returns: A boolean type of True/False, or None when there is a problem in execution'''
        try:
            cursor = self.connection.cursor()
            query = "SELECT food FROM food_information WHERE LOWER(food)=%s"
            cursor.execute(query, (food_name.lower(), ))

            if cursor.fetchall() == []:
                return False
            return True

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
        
    def get_food_list(self):
        '''Arguments: None
        Purpose: Retrieve and return all the food in the table.
        Returns: A list of food'''
        try:
            cursor = self.connection.cursor()
            query = "SELECT food FROM food_information"
            cursor.execute(query)

            return cursor.fetchall()

        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
        
if __name__ == '__main__':
    my_source = DataSource()
    print(my_source.get_food_allergy("Sweet and Spicy Sriracha Sauce", "wheat")) 
   