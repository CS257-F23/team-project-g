import sys
import csv
data = []
usage_calories = ("Usage : python3 Production/basic_cl.py -calories 'food'"
            "Note: only one food option is required after '-calories', food name of multiple words shoule be put in quotes")
usage_diet = ("Usage : python3 Production/basic_cl.py -diet 'food1' ['food2' ... ]"
            "Note: at least one food option is required after '-diet', multiple food items are valid as well")

def load_data():
    '''Arguments: None
Return value: the whole data set, in the format of a dictionary
Purpose: load data for future function use'''
    global data

    file = open("Data/CFAfacts.csv", encoding="utf-8")

    for line in file:
        line = line.strip()
        fields = line.split(",")

        # Create a dictionary for each row
        row = {
                'Item': fields[0],
                'Size': fields[1],
                'Calories': fields[2],
                'Fat': fields[3],
                'SaturatedFat': fields[4],
                'TransFat': fields[5],
                'Cholesterol': fields[6],
                'Sodium': fields[7],
                'Carbohydrates': fields[8],
                'Fiber': fields[9],
                'Sugar': fields[10],
                'Protein': fields[11],
                'Dairy': fields[12],
                'Egg': fields[13],
                'Soy': fields[14],
                'Wheat': fields[15],
                'Tree Nuts': fields[16],
                'Fish': fields[17]
        }

        data.append(row)

    data.pop(0) # remove header
    return data

def get_value(row, column):
    '''Arguments: row number and column name
    Return value: the value in that cell
    Purpose: get data from dataset'''
    return data[row][column]

def get_row(food_name):
    '''Arguments: name of the food(string)
Return value: the row that the food value is in
Purpose: get the row of a specified food'''
    global data
    target_food = food_name.lower()
    target_row = 0
    match = 0
    for row in range(len(data)):
        if get_value(row, "Item").lower() == target_food:
            match += 1
            target_row = row
            return target_row
    if match == 0:
        return -1

def get_calories_by_name(food_name):
    '''Arguments: name of the food(string)
Return value: the calories column of the row that the food is in, or if it is not in the list, return a message
Purpose: get calories of a specified food'''
    global data
    target_row = get_row(food_name)

    if target_row == -1:
        return "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
    return get_value(target_row, "Calories")

def get_row_index(food_names):
    '''Arguments: a list of food names
Return value: a list of indices of corresponding columns
Purpose: get row indices in the data set for a given food names'''
    global data
    row_index = []
    for item in food_names:
        row_index.append(get_row(item))
    return row_index

def get_sum(index, allergies):
    '''Arguments: a list of indices, and an string of a given allergy item
    Return value: an integer, marking whether food in the index list cotains the given allergies (0) or not
    Purpose: checking whether food in the index list cotains the given allergies (0) or not'''
    global data
    sum = 0
    for row in index:
        if data[row][allergies] == "1":
            sum = sum + 1
    return sum

def check_list_invalidity(food_index):
    '''Arguments: a list of food
    Return value: -1 if any of the food in the list is not found in the dataset
    Purpose: checking whether foods are in the dataset'''
    for index in food_index:
        if index == -1:
            return True

def get_allergy_sums(food_index_list, allergy_list):
    '''Arguments: a list of food indices, an allergy list
    Return value: a list of sums of allergy list
    Purpose: getting sum of indicator rows of all allergies (how many food in list have
    allergies specified)'''
    sum_list = []
    for allergy_items in allergy_list:
        this_sum = get_sum(food_index_list, allergy_items)
        sum_list.append(this_sum)
    return sum_list

def print_restriction(allergy_sum_list, allergy_list):
    '''Arguments: a list of allergy sums, an allergy list
    Return value: a list of allergy items that has non-zero occurences
    Purpose: print allergies specified in the list of food'''
    output = []
    for i in range(len(allergy_sum_list)):
        if allergy_sum_list[i] != 0:
            output.append(allergy_list[i])
    return output

def get_restriction(food_list):
    '''Arguments: a list of food
    Return value: an integer, marking whether food in the index list cotains the given allergies (0) or not
    Purpose: checking whether food in the index list cotains the given allergies (0) or not'''
    global data
    food_index = get_row_index(food_list)
    if check_list_invalidity(food_index):
        return usage_diet
    allergy_lst = ["Dairy","Egg","Soy","Wheat","Tree Nuts","Fish"]
    sum_list = get_allergy_sums(food_index, allergy_lst)

    return print_restriction(sum_list, allergy_lst)

def msg_calories(argument):
    '''Arguments: a list of command line arguments for calories function
    Return value: the message shown to users
    Purpose: helper function for main() to print message out'''
    if len(argument) != 3:
        return usage_calories
    else:
        return get_calories_by_name(sys.argv[2])
    
def msg_diet(argument):
    '''Arguments: a list of command line arguments for diet function
    Return value: the message shown to users
    Purpose: helper function for main() to print message out'''
    if len(argument) <= 2:
        return usage_diet
    else:
        return get_restriction(sys.argv[2:])
    
def msg():
    '''Arguments: none
    Return value: the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    return "usage method not found, please use one of the usage method below: \n" + usage_calories + usage_diet

def check_sysArgv(position, argument):
    '''Arguments: the position of the command line input we want to check, and an expected argument
    Return value: the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    return sys.argv[position] == argument

def print_msg(command_line):
    '''Arguments: a list of command line
    Return value: the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    if check_sysArgv(1, "-calories"):
        return msg_calories(command_line)
    
    elif check_sysArgv(1, "-diet"):
        return msg_diet(command_line)

    else:
        return msg()

def main():
    '''Arguments: None
Return value: None
Purpose: Maintains command line interface, loads data. Usage statement: "Usage: python3 ProductionCode/basic_cl.py -method method_param". Returns relevant information as desired.'''
    load_data()
    print(print_msg(sys.argv))

if __name__ == "__main__":
    main()