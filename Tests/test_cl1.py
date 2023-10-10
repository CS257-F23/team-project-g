import subprocess
import unittest
from ProductionCode.basic_cl import *

#variables for usage statement
usage_calories = ("Usage : python3 Production/basic_cl.py -calories 'food'\n"
        "Note: only one food option is required after '-calories', food name of multiple words shoule be put in quotes")
usage_diet = ("Usage : python3 Production/basic_cl.py -diet 'food1' ['food2' ... ]\n"
        "Note: at least one food option is required after '-diet', multiple food items are valid as well")

class Test_get_calories_by_name(unittest.TestCase):
    
    #base case
    def test_get_value_normal(self):
        """Purpose: Check if get_value works for valid row/column input"""
        value = get_value(2, "Size")
        expected = '59g'
        self.assertEqual(value, expected)
    
    #edge case
    def test_get_value_edge(self):
        """Purpose: Check if get_value works for edge row/column input (last entry)"""
        value = get_value(240, "Fish")
        expected = '0'
        self.assertEqual(value, expected)

    #base case
    def test_get_row_normal(self):
        """Purpose: Check if get_row works for valid food"""
        row = get_row("Barbeque Sauce")
        expected = 3
        self.assertEqual(row, expected)

    #edge case
    def test_get_row_invalid(self):
        """Purpose: Check if get_row works for invalid food"""
        row = get_row("Charlie")
        expected = -1
        self.assertEqual(row, expected)
    
    #base case
    def test_get_calories_by_name_allcorrect1(self):
        """Purpose: Check if get_calories_by_name works for valid food item."""
        calories=get_calories_by_name('Coffee')
        expected = '0'
        self.assertEqual(calories, expected)
    
    #base case
    def test_get_calories_by_name_capitalerror(self):
        """Purpose: Check if get_calories_by_name() works for valid food item with wrong capitalizaton."""
        calories=get_calories_by_name('PEAch Milkshake')
        expected = '590'
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
    def test_get_row_index_normal(self):
        """Purpose: Check if get_row_index works for valid food list"""
        fd_list = ["Chocolate Milkshake", "Strawberry Milkshake"]
        index = get_row_index(fd_list)
        expected = [17, 18]
        self.assertEqual(index, expected)

    #edge case
    def test_get_row_index_invalid(self):
        """Purpose: Check if get_row_index works for food list containing food not in original data"""
        fd_list = ["Chocolate Milkshake", "Strawberry Milkshake", "Charlie"]
        index = get_row_index(fd_list)
        expected = [17, 18, -1]
        self.assertEqual(index, expected)

    #base case
    def test_get_sum_normal(self):
        """Purpose: Check if get_sum works for valid index list and allergy"""
        index_lst = [12, 25, 38]
        allergy = "Fish"
        expected = 0
        self.assertEqual(get_sum(index_lst, allergy), expected)
    
    #edge case
    def test_get_sum_edge(self):
        """Purpose: Check if get_sum works for edge case index list and allergy (first + last entry)"""
        index_lst = [0, 240]
        allergy = "Dairy"
        expected = 2
        self.assertEqual(get_sum(index_lst, allergy), expected)

    #base case
    def test_check_list_invalidity_normal(self):
        """Purpose: Check if check_list_invalidity works for valid index list"""
        food_index = [12, 25, 38]
        expected = None
        self.assertEqual(check_list_invalidity(food_index), expected)

    #edge case
    def test_check_list_invalidity_invalid(self):
        """Purpose: Check if check_list_invalidity works for invalid index list"""
        food_index = [12, 25, -1]
        expected = True
        self.assertEqual(check_list_invalidity(food_index), expected)
    
    #base case
    def test_get_allergy_sums_normal(self):
        """Purpose: Check if get_allergy_sums works for valid index list and allergy list"""
        food_index = [12, 25, 38]
        allergy_lst = ["Dairy",	"Egg", "Soy"]
        expected = [1,0,0]
        self.assertEqual(get_allergy_sums(food_index, allergy_lst), expected)
        
    #base case
    def test_get_allergy_sums_normal(self):
        """Purpose: Check if get_allergy_sums works for edge case valid index list and allergy list
        first + last entry"""
        food_index = [0, 240]
        allergy_lst = ["Dairy",	"Fish"]
        expected = [2,0]
        self.assertEqual(get_allergy_sums(food_index, allergy_lst), expected)

    #base case
    def test_print_restriction_normal(self):
        """Purpose: Check if print_restriction works for valid allergy sum list and allergy list"""
        allergy_sum_lst = [2, 1, 0]
        allergy_lst  = ["Dairy", "Egg", "Soy"]
        expected = ["Dairy", "Egg"]
        self.assertEqual(print_restriction(allergy_sum_lst, allergy_lst), expected)

    #edge case
    def test_print_restriction_edge(self):
        """Purpose: Check if print_restriction works for edge allergy sum list and allergy list,
        (no indicator of allergy exists (they are all 0))"""
        allergy_sum_lst = [0, 0, 0, 0, 0, 0]
        allergy_lst  = ["Dairy","Egg","Soy","Wheat","Tree Nuts","Fish"]
        expected = []
        self.assertEqual(print_restriction(allergy_sum_lst, allergy_lst), expected)

    #base case
    def test_get_restriction_one_food(self):
        """Purpose: Check if get_restriction() works for a list with one valid food item"""
        food = ["Crispy Bell Peppers"]
        expected = ["Wheat"]
        self.assertCountEqual(get_restriction(food),expected)
    
    #base case
    def test_get_restriction_two_food(self):
        """Purpose: Check if get_restriction() works for a list with two valid food items"""
        food = ["Crispy Bell Peppers", "Garden Herb Ranch Dressing"]
        expected = ["Dairy", "Egg", "Wheat"]
        self.assertCountEqual(get_restriction(food),expected)

    #base case
    def test_get_restriction_five_food(self):
        """Purpose: Check if get_restriction() works for a list with five valid food items"""
        food = ["Crispy Bell Peppers", "Garden Herb Ranch Dressing","Roasted Nut Blend", "5 Ct Nuggets Kid's Meal", "Tomato"]
        expected = ["Dairy", "Egg", "Wheat", "Tree Nuts"]
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
        expected = "0"
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
        expected = ['Dairy', 'Egg', 'Wheat']
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
        expected = '0'
        self.assertEqual(print_msg(command), expected)

    #base case
    def test_print_msg_diet(self):
        """Purpose: Check if print_msg works for valid diet command line argument input"""
        command = ["Production/basic_cl.py", "-diet", "Crispy Bell Peppers", "Garden Herb Ranch Dressing"]
        expected = ['Dairy', 'Egg', 'Wheat']
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