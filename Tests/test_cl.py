import subprocess
import unittest
from ProductionCode.basic_cl import *

class Test_get_calories_by_name(unittest.TestCase):

    
    def test_get_calories_by_name_allcorrect(self):
        """Check if get_calories_by_name works for valid food item."""
        calories=get_calories_by_name('Hotcakes')
        self.assertEqual(calories, 350)
    
    def test_get_calories_by_name_capitalerror(self):
        """Check if get_calories_by_name() works for valid food item with wrong capitalizaton."""
        calories=get_calories_by_name('HAmhurger')
        self.assertEqual(calories, 240)
    
    def test_get_calories_by_name_wrongfood(self):
        """Check if get_calories_by_name() raises Value error for invalid food item."""
        self.assertRaises(ValueError, get_calories_by_name, 'Charlie')
        
    def test_get_calories_by_name_commandcorrect(self):
        """Check if basic_cl.py works for valid 'calories' command line arguments."""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        food="'Egg McMuffin'"
        code = subprocess.Popen(['python3', file_path,'-calories', food], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        expected=300
        self.assertEqual(output.strip(), expected) 
        code.terminate()
    
    def test_get_calories_by_name_commanderror(self):
        """Check if basic_cl.py works for invalid '-calories' command line arguments"""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, '-calories'], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertIn(output.strip(), "Usage: python3 basic_cl.py -calories 'food'")
        code.terminate()
    
    def test_commanderror(self):
        """Check if basic_cl.py works for invalid command line arguments"""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, '-Charlie'], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertIn(output.strip(), "Usage:\n get food calories: python3 basic_cl.py -calories 'food'"
                      " \n get food allergies: python3 ____.py -diet 'food1' 'food2'")
        code.terminate()
    
class Test_get_foodlist_without_allergy(unittest.TestCase):
    
    
    def test_get_foodlist_without_allergy_allcorrect(self):
        foodlist=get_foodlist_without_allergy('egg')
        self.assertCountEqual(foodlist, ['Crispy Bell Peppers','Roasted Nut Blend','Seasoned Tortilla Strips','Hash Browns'])
    


    
load_data()
if __name__ == '__main__':
    unittest.main()