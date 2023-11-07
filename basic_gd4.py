import sys
from ProductionCode.datasource import DataSource

data = []
usage_calories = ("Usage : python3 Production/basic_gd4.py -calories 'food'\n"
            "Note: only one food option is required after '-calories', food name of multiple words shoule be put in quotes")
usage_diet = ("Usage : python3 Production/basic_gd4.py -diet 'food1' ['food2' ... ]\n"
            "Note: at least one food option is required after '-diet', multiple food items are valid as well")

data_source = None

def get_data_source():
    global data_source
    if data_source is None:
        data_source = DataSource()
    return data_source


def get_restriction(food_list):
    '''Arguments: a list of food
    Return value: a list of allergies, which includes all the allergens contained for the food list inputted.'''
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
    Purpose: check if the food item exists in the database'''
    get_data_source()
    return data_source.food_exist(food)

def get_restriction_item(food, allergies_sum):
    '''Arguments: a food item and a list of allergens
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
    Return value: the calories column of the row that the food is in, or if it is not in the list, return a message
    Purpose: get calories of a specified food'''
    get_data_source()
    if food_exist(food) == False:
        return False
    calorie = data_source.get_calorie_from_table(food)
    return calorie[0][0]
    

# #load the data from CFAfacts.csv
# def load_data():
#     '''Arguments: None
#     Return value: the whole data set, in the format of a dictionary
#     Purpose: load data for future function use'''
#     global data

#     file = open("Data/CFAfacts.csv", encoding="utf-8")

#     for line in file:
#         line = line.strip()   #remove extra white space
#         fields = line.split(",")    #seperate elements in a line using comma

#         # Create a dictionary for each row
#         row = {
#                 'Item': fields[0],
#                 'Calories': fields[1],
#                 'Dairy': fields[2],
#                 'Egg': fields[3],
#                 'Soy': fields[4],
#                 'Wheat': fields[5],
#                 'Tree Nuts': fields[6],
#                 'Fish': fields[7]
#         }

#         data.append(row)

#     file.close() #close file
#     return data


#helper function for main
def msg_calories(argument):
    '''Arguments: a list of command line arguments for calories function
    Return value: the message shown to users
    Purpose: helper function for main() to print message out'''
    if len(argument) != 3:
        return usage_calories
    else:
        msg = get_calories_by_name(argument[2])
        if msg == False:
            return "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        return msg

#helper function for main
def msg_diet(argument):
    '''Arguments: a list of command line arguments for diet function
    Return value: the message shown to users
    Purpose: helper function for main() to print message out'''
    if len(argument) <= 2:
        return usage_diet
    else:
        msg = get_restriction(argument[2:])
        if msg == False:
            return "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        return msg

#helper function for main
def msg():
    '''Arguments: none
    Return value: the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    return "usage method not found, please use one of the usage method below: \n" + usage_calories + "\n" + usage_diet

#helper function for main
def check_sysArgv(command, argument):
    '''Arguments: the position of the command line input we want to check, and an expected argument
    Return value: the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    if len(command) == 1: #no command line argument
        return False
    return command[1] == argument

#helper function for main
def print_msg(command_line):
    '''Arguments: a list of command line
    Return value: the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    if check_sysArgv(command_line, "-calories"):
        return msg_calories(command_line)
    
    elif check_sysArgv(command_line, "-diet"):
        return msg_diet(command_line)

    else:
        return msg()

#core main
def main():
    '''Arguments: None
    Return value: None
    Purpose: Maintains command line interface, loads data. Usage statement: "Usage: python3 ProductionCode/basic_gd4.py -method method_param". Returns relevant information as desired.'''
    load_data()
    print(print_msg(sys.argv))
    
    

if __name__ == "__main__":
    main()