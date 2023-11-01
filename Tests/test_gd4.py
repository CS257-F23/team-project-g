import subprocess
import unittest
from ProductionCode.basic_gd4 import *

#variables for usage statement
usage_calories = ("Usage : python3 Production/basic_cl.py -calories 'food'\n"
        "Note: only one food option is required after '-calories', food name of multiple words shoule be put in quotes")
usage_diet = ("Usage : python3 Production/basic_cl.py -diet 'food1' ['food2' ... ]\n"
        "Note: at least one food option is required after '-diet', multiple food items are valid as well")

class Test_get_calories_by_name(unittest.TestCase):
    
    #base case
    def test_get_calories_by_name_allcorrect1(self):
        """Purpose: Check if get_calories_by_name works for valid food item."""
        calories=get_calories_by_name('Coffee')
        expected = 0
        self.assertEqual(calories, expected)
    
    #base case
    def test_get_calories_by_name_capitalerror(self):
        """Purpose: Check if get_calories_by_name() works for valid food item with wrong capitalizaton."""
        calories=get_calories_by_name('PEAch Milkshake')
        expected = 590
        self.assertEqual(calories, expected)
    
    #edge case
    def test_get_calories_by_name_wrongfood(self):
        """Purpose: Check if get_calories_by_name() output warning for invalid food item."""
        food = "Charlie"
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path,'-calories', food], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertEqual(output.strip(), 'Sorry, the item you are searching for is not in the menu of Chick-fil-A.') 
        code.terminate()
    
    #base_case
    def test_get_calories_by_name_commandcorrect(self):
        """Purpose: Check if basic_cl.py works for valid 'calories' command line arguments."""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path,'-calories', 'Coffee'], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        expected = '0'
        self.assertEqual(output.strip(), expected) 
        code.terminate()
    
    #edge_case
    def test_get_calories_by_name_commanderror(self):
        """Purpose: Check if basic_cl.py works for invalid '-calories' command line arguments"""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, '-calories'], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertEqual(output.strip(), usage_calories)
        code.terminate()
    
    #edge case
    def test_commanderror(self):
        """Purpose: Check if basic_cl.py works for invalid command line arguments"""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        expected = ("usage method not found, please use one of the usage method below: \n" 
                    + usage_calories + "\n" 
                    + usage_diet)
        code = subprocess.Popen(['python3', file_path, '-Charlie'], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertEqual(output.strip(), expected)
        code.terminate()

class Test_get_restriction(unittest.TestCase):
    #base case
    def test_get_restriction_one_food(self):
        """Purpose: Check if get_restriction() works for a list with one valid food item"""
        food = ["Crispy Bell Peppers"]
        expected = ["wheat"]
        self.assertCountEqual(get_restriction(food),expected)
    
    #base case
    def test_get_restriction_two_food(self):
        """Purpose: Check if get_restriction() works for a list with two valid food items"""
        food = ["Crispy Bell Peppers", "Garden Herb Ranch Dressing"]
        expected = ["dairy", "egg", "wheat"]
        self.assertCountEqual(get_restriction(food),expected)

    #base case
    def test_get_restriction_five_food(self):
        """Purpose: Check if get_restriction() works for a list with five valid food items"""
        food = ["Crispy Bell Peppers", "Garden Herb Ranch Dressing","Roasted Nut Blend", "5 Ct Nuggets Kid's Meal", "Tomato"]
        expected = ["dairy", "egg", "wheat", "nuts"]
        self.assertCountEqual(get_restriction(food),expected)

    #base case
    def test_get_restriction_main_basic(self):
        """Purpose: Check if basic_cl.py works for valid command line arguments"""
        food1 = "Crispy Bell Peppers"
        food2 = "Garden Herb Ranch Dressing"
        option = "-diet"
        expected = "['Dairy', 'Egg', 'Wheat']"
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, option, food1, food2], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate() 
        self.assertEqual(output.strip(), expected) 
        code.terminate() 

    #edge case
    def test_get_restriction_main_invalid_food(self):
        """Purpose: Check if basic_cl.py works for an argument of list containing a food item that does not exists in datasets"""
        option = "-diet"
        food = "Silly"
        expected = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, option, food], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate() 
        self.assertEqual(output.strip(), expected) 
        code.terminate() 

    #edge case
    def test_get_restriction_main_invalid(self):
        """Purpose: Check if basic_cl.py works for invalid command line arguments"""
        option = "-diet"
        expected = usage_diet
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, option], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate() 
        self.assertEqual(output.strip(), expected) 
        code.terminate() 

class Test_main_helper(unittest.TestCase):

    #base case
    def test_msg_calories_normal(self):
        """Purpose: Check if msg_calories works for valid command line argument input"""
        argument = ["Production/basic_cl.py", "-calories", "Coffee"]
        expected = 0
        self.assertEqual(msg_calories(argument), expected)

    #edge case
    def test_msg_calories_invalid(self):
        """Purpose: Check if msg_calories works for invalid command line argument input"""
        argument = ["Production/basic_cl.py", "-calories", "1%", "milk"]
        expected = usage_calories
        self.assertEqual(msg_calories(argument), expected)

    #base case
    def test_msg_diet_normal(self):
        """Purpose: Check if msg_diet works for valid command line argument input"""
        argument = ["Production/basic_cl.py", "-diet", "Crispy Bell Peppers", "Garden Herb Ranch Dressing"]
        expected = ['dairy', 'egg', 'wheat']
        self.assertEqual(msg_diet(argument), expected)

    #edge case
    def test_msg_diet_invalid(self):
        """Purpose: Check if msg_diet works for invalid command line argument input"""
        argument = ["Production/basic_cl.py", "-diet"]
        expected = usage_diet
        self.assertEqual(msg_diet(argument), expected)

    #base case
    def test_msg(self):
        """Purpose: Check if msg works"""
        expected = "usage method not found, please use one of the usage method below: \n" + usage_calories + "\n" + usage_diet
        self.assertEqual(msg(), expected)
    
    #base case
    def test_check_sysArgv_calories(self):
        """Purpose: Check if check_sysArgv works for valid calories command line argument input"""
        command = ["Production/basic_cl.py", "-calories", "Coffee"]
        argument = "-calories"
        expected = True
        self.assertEqual(check_sysArgv(command, argument), expected)

    #base case
    def test_check_sysArgv_diet(self):
        """Purpose: Check if check_sysArgv works for valid diet command line argument input"""
        command = ["Production/basic_cl.py", "-diet"]
        argument = "-diet"
        expected = True
        self.assertEqual(check_sysArgv(command, argument), expected)

    #edge case
    def test_check_sysArgv_invalid(self):
        """Purpose: Check if check_sysArgv works for invalid command line argument input"""
        command = ["Production/basic_cl.py", "-Charlie"]
        argument = "-calories"
        expected = False
        self.assertEqual(check_sysArgv(command, argument), expected)

    #base case
    def test_print_msg_calories(self):
        """Purpose: Check if print_msg works for valid calories command line argument input"""
        command = ["Production/basic_cl.py", "-calories", "Coffee"]
        expected = 0
        self.assertEqual(print_msg(command), expected)

    #base case
    def test_print_msg_diet(self):
        """Purpose: Check if print_msg works for valid diet command line argument input"""
        command = ["Production/basic_cl.py", "-diet", "Crispy Bell Peppers", "Garden Herb Ranch Dressing"]
        expected = ['dairy', 'egg', 'wheat']
        self.assertEqual(print_msg(command), expected)

    #edge case
    def test_print_msg_invalid(self):
        """Purpose: Check if print_msg works for invalid command line argument input"""
        command = ["Production/basic_cl.py", "-Charlie"]
        expected = "usage method not found, please use one of the usage method below: \n" + usage_calories + "\n" + usage_diet
        self.assertEqual(print_msg(command), expected)

load_data()
if __name__ == '__main__':
    unittest.main()