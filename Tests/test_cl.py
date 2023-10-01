import subprocess
import unittest

class Test_command_line(unittest.TestCase):
    #testing get_cell (basic test)
    def test_main(self):
        """Check if basic_cl.py works for valid command line arguments"""
        row = '0'
        column = '0'
        expected = "column_1"
        file_path = 'ProductionCode/basic_cl.py' #path to the production code
        code = subprocess.Popen(['python3', file_path, row, column], 
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8') 
        output, err = code.communicate() 
        self.assertEqual(output.strip(), expected) 
        code.terminate() 

    
        
if __name__ == '__main__':
    unittest.main()