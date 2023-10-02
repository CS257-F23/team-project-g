import subprocess
import unittest
from ProductionCode.basic_cl import *

class Test_get_calories_by_name(unittest.TestCase):

    
    def test_get_calories_by_name_allcorrect1(self):
        """Check if get_calories_by_name works for valid food item."""
        calories=get_calories_by_name('Coffee')
        self.assertEqual(calories, '0')
    
    def test_get_calories_by_name_capitalerror(self):
        """Check if get_calories_by_name() works for valid food item with wrong capitalizaton."""
        calories=get_calories_by_name('PEAch Milkshake')
        self.assertEqual(calories, '590')
    
    def test_get_calories_by_name_wrongfood(self):
        """Check if get_calories_by_name() output warning for invalid food item."""
        food = "Charlie"
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path,'-calories', food], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertEqual(output.strip(), 'Sorry, the item you are searching for is not in the menu of Chick-fil-A.') 
        code.terminate()


        
    def test_get_calories_by_name_commandcorrect(self):
        """Check if basic_cl.py works for valid 'calories' command line arguments."""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path,'-calories', 'Coffee'], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertEqual(output.strip(), '0') 
        code.terminate()
    
    def test_get_calories_by_name_commanderror(self):
        """Check if basic_cl.py works for invalid '-calories' command line arguments"""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, '-calories'], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertEqual(output.strip(), "Usage: python3 ProductionCode/basic_cl.py -calories 'food'")
        code.terminate()
    
    def test_commanderror(self):
        """Check if basic_cl.py works for invalid command line arguments"""
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        expected = ("usage method not found, please use one of the usage method below: \n"
           "Usage: python3 ProductionCode/basic_cl.py -calories 'food'\n"
           "Usage: python3 ProductionCode/basic_cl.py -diet 'food1' 'food2'")
        code = subprocess.Popen(['python3', file_path, '-Charlie'], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate()
        self.assertEqual(output.strip(), expected)
        code.terminate()


    
load_data()
if __name__ == '__main__':
    unittest.main()