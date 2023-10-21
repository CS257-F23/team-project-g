from app_gd2 import *  
import unittest

class Test_flask_html(unittest.TestCase):
    
    #base case
    def test_home_page(self):
        '''check if app.py works for the homepage (route '/') '''
        self.app = app.test_client()
        route = '/'
        response = self.app.get(route, follow_redirects=True)
        expected_pt1 = "To get calories by food name: access http://XXX.X.X.X:YYYY/calorie/food"
        expected_pt2 = "To get restrictions by food name: access http://XXX.X.X.X:YYYY/diet/food"
        self.assertIn(expected_pt1, response.data.decode('utf-8'))
        self.assertIn(expected_pt2, response.data.decode('utf-8'))

    #base case
    def test_calorie_route(self):
        '''check if app.py works for valid route for /calorie'''
        self.app = app.test_client()
        route = '/calorie/Hash Browns'
        response = self.app.get(route, follow_redirects=True)
        expected = "Calorie count of Hash Browns is 270."
        self.assertIn(expected, response.data.decode('utf-8'))

    #edge case
    def test_calorie_route_invalid(self):
        '''check if app.py works for valid route /calorie but invalid argument()'''
        self.app = app.test_client()
        route = '/calorie/Silly'
        response = self.app.get(route, follow_redirects=True)
        expected = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        self.assertIn(expected, response.data.decode('utf-8'))

    #edge case
    def test_calorie_invalid(self): #test for 404 error
        '''check if app.py works for invalid (non-existing) route, 404 page'''
        self.maxDiff = None
        self.app = app.test_client()
        route = '/calories/Hash Browns'
        response = self.app.get(route, follow_redirects=True)
        expected = "Oops, the page you were looking for doesn\'t exist, please refer to homepage or go to one of the pages below:"
        self.assertIn(expected, response.data.decode('utf-8'))

    #base case
    def test_calorie_message_not_found(self):
        '''check if calorie_message works for an argument indicating food item not found'''
        food = "McDonald Burger"
        result = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        expected = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        self.assertEqual(calories_message(result,food), expected)
    
    #base case
    def test_calorie_message_base(self):
        '''check if calorie_message works for valid calorie and food item argument'''
        food = "Tomato"
        result = "5"
        expected = "Calorie count of Tomato is 5."
        self.assertEqual(calories_message(result, food), expected)

    #base case
    def test_diet_route_valid(self):
        '''check if app.py works for valid route and argument for /diet'''
        self.app = app.test_client()
        route = '/diet/Hash Browns,Tomato,Garden Herb Ranch Sauce'
        response = self.app.get(route, follow_redirects=True)
        expected_pt1 = "Egg"
        expected_pt2 = "Dairy"
        self.assertIn(expected_pt1, response.data.decode('utf-8'))
        self.assertIn(expected_pt2, response.data.decode('utf-8'))

    #edge case
    def test_diet_route_invalid(self):
        '''check if app.py works for valid route /diet but invalid argument()'''
        self.app = app.test_client()
        route = '/diet/Silly'
        response = self.app.get(route, follow_redirects=True)
        expected = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        self.assertIn(expected, response.data.decode('utf-8'))

    #base case
    def test_diet_message_base(self):
        '''check if diet_message works for valid result argument'''
        result = ['Dairy','Egg']
        expected = "Your food include(s) 'Dairy', 'Egg'. Pay attention!"
        self.assertIn(diet_message(result), expected)
    
    #base case
    def test_diet_message_empty_list(self):
        '''check if diet_message works for empty list argument'''
        result = []
        expected = "Your food include(s) no allergies. Have fun!"
        self.assertIn(diet_message(result), expected)

    #base case
    def test_diet_message_not_found(self):
        '''check if diet_message works for an argument indicating food item not found'''
        result = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        expected = "Sorry, the item you are searching for is not in the menu of Chick-fil-A."
        self.assertEqual(diet_message(result), expected)

    #base case
    def test_split_food_input(self):
        '''check if split_food_input() works for valid list argument'''
        food = "Tomato,Honey Roasted BBQ Sauce,Coffee"
        expected = ["Tomato","Honey Roasted BBQ Sauce","Coffee"]
        self.assertCountEqual(split_food_input(food), expected) #checking whether two lists have the same element
    
if __name__=="__main__":
    unittest.main()