from ProductionCode.datasource import DataSource

class Controller:
    data_source = None

    def __init__(self):
        '''
        Arguments: Controller object
        Return value: None
        Purpose: Constructor for the Controller class that create a DataSource instance'''
        self.data_source = DataSource()

    def get_restriction(self, food_list):
        '''Arguments: a list of food
        Return value: (list) a list of allergies, which includes all the allergens contained for the food list inputted, or (Boolean) a boolean indicating that the food does not exist.
        Purpose: Give the users a list of allergies that their chosen food(s) contain'''
        allergies_sum = [0,0,0,0,0,0]
        for food in food_list:
            if self.food_exist(food) == False:
                return False
            self.get_restriction_item(food, allergies_sum)
        while 0 in allergies_sum:
            allergies_sum.remove(0)
        return allergies_sum

    def food_exist(self, food):
        '''Argument: a food item
        Return Value: (Boolean) Boolean type of True/False, indicating if the food exists in our database
        Purpose: check if the food item exists in the database'''
        return self.data_source.food_exist(food)

    def get_restriction_item(self, food, allergies_sum):
        '''Arguments: a food item and a list of allergens
        Return Value: None
        Purpose: update the allergy list with each iteration of the function checking each item.'''
        allergies = ["dairy", "egg","soy","wheat","nuts","fish"]
        cnt = 0
        for allergy in allergies:
            row =  self.data_source.get_food_allergy(food, allergy)
            if (row != None and len(row) != 0):
                allergies_sum[cnt] = allergy
            cnt += 1
        return None

    def get_calories_by_name(self, food):
        '''Arguments: name of the food(string)
        Return value: (Integer) the calories column of the row that the food is in, or (Boolean) a boolean indicating that the food does not exist
        Purpose: get calories of a specified food'''
        if self.food_exist(food) == False:
            return False
        calorie = self.data_source.get_calorie_from_table(food)
        return calorie[0][0]
    
    def get_food_list(self):
        '''Arguments: None
        Return value: (list) a list of all the food in the database
        Purpose: get a list of all the food in the database'''
        food_list = self.data_source.get_food_list()
        index = 0
        for food in food_list:
            food = str(food)
            food_list[index] = food[2:-3]
            index += 1
        return food_list