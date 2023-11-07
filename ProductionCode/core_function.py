from ProductionCode.datasource import DataSource

data_source = None

def get_data_source():
    global data_source
    if data_source is None:
        data_source = DataSource()
    return data_source


def get_restriction(food_list):
    '''Arguments: a list of food
    Return value: (list) a list of allergies, which includes all the allergens contained for the food list inputted, or (Boolean) a boolean indicating that the food does not exist.
    Purpose: Give the users a list of allergies that their chosen food(s) contain'''
    get_data_source()
    allergies_sum = [0,0,0,0,0,0]
    for food in food_list:
        if food_exist(food) == False:
            return False
        get_restriction_item(food, allergies_sum)
    while 0 in allergies_sum:
        allergies_sum.remove(0)
    return allergies_sum

def food_exist(food):
    '''Argument: a food item
    Return Value: (Boolean) Boolean type of True/False, indicating if the food exists in our database
    Purpose: check if the food item exists in the database'''
    get_data_source()
    return data_source.food_exist(food)

def get_restriction_item(food, allergies_sum):
    '''Arguments: a food item and a list of allergens
    Return Value: None
    Purpose: update the allergy list with each iteration of the function checking each item.'''
    get_data_source()
    allergies = ["dairy", "egg","soy","wheat","nuts","fish"]
    cnt = 0
    for allergy in allergies:
        row =  data_source.get_food_allergy(food, allergy)
        if (row != None and len(row) != 0):
            allergies_sum[cnt] = allergy
        cnt += 1
    return None

def get_calories_by_name(food):
    '''Arguments: name of the food(string)
    Return value: (Integer) the calories column of the row that the food is in, or (Boolean) a boolean indicating that the food does not exist
    Purpose: get calories of a specified food'''
    get_data_source()
    if food_exist(food) == False:
        return False
    calorie = data_source.get_calorie_from_table(food)
    return calorie[0][0]