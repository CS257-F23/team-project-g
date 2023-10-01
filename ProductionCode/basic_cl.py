import sys
import csv

def load_data():
    data = []

    file = open("C:/Users/22382/team-project-g/Data/CFAfacts.csv", encoding="utf-8")   

    for line in file:
        line = line.strip()
        fields = line.split(",")

        item = fields[0]
        size = fields[1]
        calories = fields[2]
        sat = fields[3]
        trans = fields[4]
        cholesterol = fields[5]
        sodium = fields[6]
        carbo = fields[7]
        fiber = fields[8]
        sugar = fields[9]
        protein = fields[10]
        dairy = fields[11]
        egg = fields[12]
        soy = fields[13]
        wheat = fields[14]
        tree = fields[15]
        fish = fields[16]

        # Create a dictionary for each row
        row = {
                'Item': item,
                'Size': size,
                'Calories': calories,
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
                'TreeNuts': tree,
                'Fish': fish
        }

        data.append(row)
    
    data.pop(0) # remove header
    return data


def load_data_subset():
    data = []

    file = open("CFAfact_subset.csv", encoding="utf-8")   

    for line in file:
        line = line.strip()
        fields = line.split(",")

        item = fields[0]
        size = fields[1]
        calories = fields[2]
        sat = fields[3]
        trans = fields[4]
        cholesterol = fields[5]
        sodium = fields[6]
        carbo = fields[7]
        fiber = fields[8]
        sugar = fields[9]
        protein = fields[10]
        dairy = fields[11]
        egg = fields[12]
        soy = fields[13]
        wheat = fields[14]
        tree = fields[15]
        fish = fields[16]

        # Create a dictionary for each row
        row = {
                'Item': item,
                'Size': size,
                'Calories': calories,
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
                'TreeNuts': tree,
                'Fish': fish
        }

        data.append(row)
    
    data.pop(0) # remove header
    return data




def get_calories_by_name(value, dataset):
    target_value = value.lower()
    target_row = 0
    for row in range(len(dataset)):
        if dataset[row]["Item"].lower() == target_value:
            target_row = row
    print(dataset[target_row]["Calories"])

    if target_row == 0:
        raise ValueError("Sorry, the item you are searching is not in the menu of Chick-fil-A.")

def get_row_index(input, dataset):
    index = []
    for row in range(len(dataset)):
        if dataset[row]["Item"] in input:
            index.append(row)
    return index

def get_sum(index, dataset, allergies):
    sum = 0
    for row in index:
        if dataset[row][allergies] == 1:
            sum += 1
    return sum

def get_restriction(input, dataset):
    input_index = get_row_index(input, dataset)
    lst = ["Dairy","Egg","Soy","Wheat","Tree Nuts","Fish"]
    result = []
    for allergy_items in lst:
        this_sum = get_sum(input_index, dataset, allergy_items)
        result.append(this_sum)
    
    output = []
    for i in range(len(result)):
        if result[i] != 0:
            output.append(lst[i])
    return output

def main():
    original_data = load_data()
    
    if sys.argv[1] == "-calories":
        if sys.argv.length() != 3:
            raise ValueError("Usage: python3 basic_cl.py -calories 'food'")
        get_calories_by_name(sys.argv[2], original_data)
    
    # if sys.argv[1] == "-diet":
    #     get_restrictions()