'''This file should contain one (or maybe a few more) functions that return hard-coded data for your Flask app to use.'''


def get_calorie(food):
    '''dummy function to return calorie of 99'''
    return 99

def get_restriction(food):
    '''dummy function to retun list of food allergies'''
    if (len(food)%2 == 1):
        return "Dairy, Egg, Soy."
    return ""

def main():
    '''main function (currently does nothing)'''
    return

if __name__ == "__main__":
    main()