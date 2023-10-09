from app import *
import unittest

class Test_flask_html(unittest.TestCase):
    def test_home_page(self):
        '''check if app.py works for the homepage (route '/') '''
        self.app = app.test_client()
        route = '/'
        response = self.app.get(route, follow_redirects=True)
        expected_pt1 = "To get calories by food name: access http://XXX.X.X.X:YYYY/calorie/food"
        expected_pt2 = "To get restrictions by food name: access http://XXX.X.X.X:YYYY/diet/food"
        self.assertIn(expected_pt1, response.data.decode('utf-8'))
        self.assertIn(expected_pt2, response.data.decode('utf-8'))

    def test_calorie_route(self):
        '''check if app.py works for valid route for /calorie'''
        self.app = app.test_client()
        route = '/calorie/Hash Browns'
        response = self.app.get(route, follow_redirects=True)
        expected = "Calorie count of Hash Browns is 270."
        self.assertIn(expected, response.data.decode('utf-8'))

    def test_calorie_route_invalid(self):
        '''check if app.py works for valid route but invalid argument()'''
        self.app = app.test_client()
        route = '/calorie/Silly'
        response = self.app.get(route, follow_redirects=True)
        expected = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        self.assertIn(expected, response.data.decode('utf-8'))

    def test_calorie_invalid(self):
        '''check if app.py works for invalid (non-existing) route'''
        self.app = app.test_client()
        route = '/calories/Hash Browns'
        response = self.app.get(route, follow_redirects=True)
        self.assertEqual("sorry, wrong format, refer to the homepage for more info", response.data.decode('utf-8'))

    def test_message_by_result_not_found(self):
        '''check if message_by_result works for an argument indicating food item not found'''
        food = "McDonald Burger"
        result = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        expected = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        self.assertEqual(calories_message(result,food), expected)
    
    def test_message_by_result_base(self):
        '''check if message_by_result works for valid calorie and food item argument'''
        food = "Tomato"
        result = "5"
        expected = "Calorie count of Tomato is 5."
        self.assertEqual(calories_message(result, food), expected)
        
    
    


if __name__=="__main__":
    unittest.main()