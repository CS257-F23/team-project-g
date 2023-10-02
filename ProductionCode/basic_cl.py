import sys
import csv
data = []

def load_data():
    global data

    file = open("Data/CFAfacts.csv", encoding="utf-8")   

    for line in file:
        line = line.strip()
        fields = line.split(",")

        item = fields[0]
        size = fields[1]
        calories = fields[2]
        fat = fields[3]
        sat = fields[4]
        trans = fields[5]
        cholesterol = fields[6]
        sodium = fields[7]
        carbo = fields[8]
        fiber = fields[9]
        sugar = fields[10]
        protein = fields[11]
        dairy = fields[12]
        egg = fields[13]
        soy = fields[14]
        wheat = fields[15]
        tree = fields[16]
        fish = fields[17]

        # Create a dictionary for each row
        row = {
                'Item': item,
                'Size': size,
                'Calories': calories,
                'Fat': fat,
                'SaturatedFat': sat,
                'TransFat': trans,
                'Cholesterol': cholesterol,
                'Sodium': sodium,
                'Carbohydrates': carbo,
                'Fiber': fiber,
                'Sugar': sugar,
                'Protein': protein,
                'Dairy': dairy,
                'Egg': egg,
                'Soy': soy,
                'Wheat': wheat,
                'Tree Nuts': tree,
                'Fish': fish
        }

        data.append(row)

    data.pop(0) # remove header
    return data


def load_data_subset():
    global data
    
    file = open("Data/CFAfact_subset.csv", encoding="utf-8")   

    for line in file:
        line = line.strip()
        fields = line.split(",")

        item = fields[0]
        size = fields[1]
        calories = fields[2]
        fat = fields[3]
        sat = fields[4]
        trans = fields[5]
        cholesterol = fields[6]
        sodium = fields[7]
        carbo = fields[8]
        fiber = fields[9]
        sugar = fields[10]
        protein = fields[11]
        dairy = fields[12]
        egg = fields[13]
        soy = fields[14]
        wheat = fields[15]
        tree = fields[16]
        fish = fields[17]

        # Create a dictionary for each row
        row = {
                'Item': item,
                'Size': size,
                'Calories': calories,
                'Fat': fat,
                'SaturatedFat': sat,
                'TransFat': trans,
                'Cholesterol': cholesterol,
                'Sodium': sodium,
                'Carbohydrates': carbo,
                'Fiber': fiber,
                'Sugar': sugar,
                'Protein': protein,
                'Dairy': dairy,
                'Egg': egg,
                'Soy': soy,
                'Wheat': wheat,
                'Tree Nuts': tree,
                'Fish': fish
        }


        data.append(row)
    
    data.pop(0) # remove header
    return data

def get_row(value):
    '''Arguments: value(string)
Return value: the row that the food value is in
Purpose: get the row of a specified food'''
    global data
    target_value = value.lower()
    target_row = 0
    match = 0
    for row in range(len(data)):
        if data[row]["Item"].lower() == target_value:
            match += 1
            target_row = row
            return target_row
    if match == 0:
        return -1

def get_calories_by_name(value):
    '''Arguments: value(string)
Return value: the calories column of the row that the food is in
Purpose: get calories of a specified food'''
    global data
    target_row = get_row(value)

    if target_row == -1:
        print("Sorry, the item you are searching for is not in the menu of Chick-fil-A.")
        return
    return data[target_row]["Calories"]

def get_row_index(input):
    global data
    index = []
    for item in input:
        index.append(get_row(item))
    return index

def get_sum(index, allergies):
    global data
    sum = 0
    for row in index:
        if data[row][allergies] == "1":
            sum = sum + 1
    return sum

def get_restriction(input):
    global data
    input_index = get_row_index(input)
    for index in input_index:
        if index == -1:
            return "Usage : python3 Production/basic_cl.py -diet 'food1' 'food2'"
    lst = ["Dairy","Egg","Soy","Wheat","Tree Nuts","Fish"]
    result = []
    for allergy_items in lst:
        this_sum = get_sum(input_index, allergy_items)
        result.append(this_sum)

    output = []
    for i in range(len(result)):
        if result[i] != 0:
            output.append(lst[i])
    return output

def main():
    load_data()
    if sys.argv[1] == "-calories":
        if len(sys.argv) != 3:
            print("Usage: python3 ProductionCode/basic_cl.py -calories 'food'")
            return
        get_calories_by_name(sys.argv[2])
    
    elif sys.argv[1] == "-diet":
        if len(sys.argv) <= 2:
            print("Usage : python3 Production/basic_cl.py -diet 'food1' 'food2'")
        else:
            print(get_restriction(sys.argv[2:]))
    
    else:
        print("usage method not found, please use one of the usage method below: \n"+
              "Usage: python3 ProductionCode/basic_cl.py -calories 'food'\n" +
              "Usage: python3 Production/basic_cl.py -diet 'food1' 'food2'")

if __name__ == "__main__":
    main()