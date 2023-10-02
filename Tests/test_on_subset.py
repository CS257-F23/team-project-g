import subprocess
import unittest
from ProductionCode.basic_cl import *

class Test_get_restriction(unittest.TestCase):
    #testing get_cell (basic test)
    load_data_subset()
    def test_get_restriction_one_food(self):
        """Check if get_restriction() works for a list with one valid food item"""
        food = ["Crispy Bell Peppers"]
        expected = ["Wheat"]
        self.assertCountEqual(get_restriction(food),expected)
    
    def test_get_restriction_two_food(self):
        """Check if get_restriction() works for a list with two valid food items"""
        food = ["Crispy Bell Peppers", "Garden Herb Ranch Dressing"]
        expected = ["Dairy","Egg", "Wheat"]
        self.assertCountEqual(get_restriction(food),expected)

    def test_get_restriction_five_food(self):
        """Check if get_restriction() works for a list with five valid food items"""
        food = ["Crispy Bell Peppers", "Garden Herb Ranch Dressing","Roasted Nut Blend", "5 Ct Nuggets Kid's Meal", "Tomato"]
        expected = ["Dairy","Egg", "Wheat", "Tree Nuts"]
        self.assertCountEqual(get_restriction(food),expected)

    def test_get_restriction_no_food(self):
        """Check if get_restriction() raises ValueError for an argument of empty list"""
        food = []
        self.assertRaises(ValueError, get_restriction, food)
    
    def test_get_restriction_wrong_food_name(self):
        """Check if get_restriction() raises ValueError for an argument of list containing a food item that does not exists in datasets"""
        food = ["Silly"]
        self.assertRaises(ValueError, get_restriction, food)
    
    def test_get_restriction_wrong_arg_type(self):
        """Check if get_restriction() raises TypeError for an argument of string"""
        food = "Crispy Bell Peppers"
        self.assertRaises(TypeError, get_restriction, food)

    def test_get_restriction_main_basic(self):
        """Check if ____.py works for valid command line arguments"""
        food1 = "Crispy Bell Peppers"
        food2 = "Garden Herb Ranch Dressing"
        option = "-diet"
        expected = "['Dairy','Egg', 'Wheat']"
        file_path = 'ProductionCode/____.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, option, food1, food2], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate() 
        self.assertEqual(output.strip(), expected) 
        code.terminate() 

    def test_get_restriction_main_basic(self):
        """Check if basic_cl.py works for invalid command line arguments"""
        option = "-diet"
        expected = "Usage : python3 ____.py -diet 'food1' 'food2'"
        file_path = 'ProductionCode/____.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, option], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate() 
        self.assertEqual(output.strip(), expected) 
        code.terminate() 
    
        
if __name__ == '__main__':
    unittest.main()