import subprocess
import unittest
#from ProductionCode import *

class Test_command_line(unittest.TestCase):
    #testing get_cell (basic test)
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
        food = []
        self.assertRaises(ValueError, get_restriction, food)

    
        

    
        
if __name__ == '__main__':
    unittest.main()