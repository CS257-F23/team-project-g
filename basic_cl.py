import sys
import ProductionCode.core_function as core
data = []
usage_calories = ("Usage : python3 basic_cl.py -calories 'food'\n"
            "Note: only one food option is required after '-calories', food name of multiple words shoule be put in quotes")
usage_diet = ("Usage : python3 basic_cl.py -diet 'food1' ['food2' ... ]\n"
            "Note: at least one food option is required after '-diet', multiple food items are valid as well")
    
control = core.Controller()

def msg_calories(argument):
    '''Arguments: a list of command line arguments for calories function
    Return value: (string) the message shown to users
    Purpose: helper function for main() to print message out'''
    if len(argument) != 3:
        return usage_calories
    else:
        msg = control.get_calories_by_name(argument[2])
        if type(msg) is bool and msg == False :
            return "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        return msg

def msg_diet(argument):
    '''Arguments: a list of command line arguments for diet function
    Return value: (string) the message shown to users
    Purpose: helper function for main() to print message out'''
    if len(argument) <= 2:
        return usage_diet
    else:
        msg = control.get_restriction(argument[2:])
        if msg == False:
            return "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        return msg

def msg():
    '''Arguments: none
    Return value: (string) the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    return "usage method not found, please use one of the usage method below: \n" + usage_calories + "\n" + usage_diet

def check_sysArgv(command, argument):
    '''Arguments: the position of the command line input we want to check, and an expected argument
    Return value: (string) the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    if len(command) == 1: 
        return False
    return command[1] == argument

def print_msg(command_line):
    '''Arguments: a list of command line
    Return value: (string) the usage message shown to users
    Purpose: helper function for main() to print usage message out'''
    if check_sysArgv(command_line, "-calories"):
        return msg_calories(command_line)
    
    elif check_sysArgv(command_line, "-diet"):
        return msg_diet(command_line)

    else:
        return msg()

def main():
    '''Arguments: None
    Return value: None
    Purpose: Maintains command line interface, loads data. Usage statement: "Usage: python3 ProductionCode/basic_gd4.py -method method_param". Returns relevant information as desired.'''
    print(print_msg(sys.argv))
    
    

if __name__ == "__main__":
    main()