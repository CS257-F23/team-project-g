import sys
import csv

def main():



    if sys.argv[1] == "-calories":
        if sys.argv.length() != 3:
            raise ValueError("Usage: python3 basic_cl.py -calories 'food'")
        get_calories_by_name(sys.argv[2], original_data)
    
    if sys.argv[1] == "-diet":
        get_restrictions()




def get_calories_by_name(value, dataset):
    target_value = value.lower()
    target_row = "empty"
    for row in dataset:
        if dataset[row]["Item"].lower() == target_value:
            target_row = row
    print(dataset[target_row]["Calories"])

    if target_row == "empty":
        raise ValueError("Sorry, the item you are searching is not in the menu of Chick-fil-A.")


def get_restrictions():