import sys
import csv
from ProductionCode.datasource import DataSource
def get_restriction(food_list):
    '''Arguments: a list of food
    Return value: a list of allergies, which includes all the allergens contained for the food list inputted.'''
    allergies_sum = [0,0,0,0,0,0]
    for food in food_list:
        get_restriction_item(food, allergies_sum)
    while 0 in allergies_sum:
        allergies_sum.remove(0)
    return allergies_sum


def get_restriction_item(food, allergies_sum):
    '''Arguments: a food item and a list of allergens
    Purpose: update the allergy list with each iteration of the function checking each item.'''
    data_source = DataSource()
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
    data_source = DataSource()
    return data_source.get_calorie_from_table(food)

