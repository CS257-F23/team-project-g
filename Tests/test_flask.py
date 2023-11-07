from app import *  
import unittest

class Test_flask_html(unittest.TestCase):
    
    def test_home_page(self):
        '''check if app.py works for the homepage (route '/') '''
        self.app = app.test_client()
        route = '/'
        response = self.app.get(route, follow_redirects=True)
        expected_pt = "Chick-fil-A Nutrition Guide"
        self.assertIn(expected_pt, response.data.decode('utf-8'))

    def test_calorie_route(self):
        '''check if app.py works for valid route for /calorie'''
        self.app = app.test_client()
        route = '/get_calorie?option_select=Calorie&text_box=Hash+Browns&search_button=Search+🔍'
        response = self.app.get(route, follow_redirects=True)
        expected = "270"
        self.assertIn(expected, response.data.decode('utf-8'))

    def test_calorie_route_invalid(self):
        '''check if app.py works for valid route /calorie but invalid argument()'''
        self.app = app.test_client()
        route = '/get_calorie?option_select=Calorie&text_box=Silly&search_button=Search+🔍'
        response = self.app.get(route, follow_redirects=True)
        expected = "Sorry"
        self.assertIn(expected, response.data.decode('utf-8'))

    def test_calorie_invalid(self):
        '''check if app.py works for invalid (non-existing) route, 404 page'''
        self.maxDiff = None
        self.app = app.test_client()
        route = '/calories/Hash Browns'
        response = self.app.get(route, follow_redirects=True)
        expected = "Oops"
        self.assertIn(expected, response.data.decode('utf-8'))
        
    def test_diet_route_valid(self):
        '''check if app.py works for valid route and argument for /diet'''
        self.app = app.test_client()
        route = '/get_diet?option_select=Allergy&text_box=Hash+Browns%2CTomato%2CGarden+Herb+Ranch+Sauce&search_button=Search+🔍'
        response = self.app.get(route, follow_redirects=True)
        expected_pt = "dairy"
        self.assertIn(expected_pt, response.data.decode('utf-8'))

    def test_diet_route_invalid(self):
        '''check if app.py works for valid route /diet but invalid argument()'''
        self.app = app.test_client()
        route = '/get_diet?option_select=Allergy&text_box=Silly&search_button=Search+🔍'
        response = self.app.get(route, follow_redirects=True)
        expected = "Sorry"
        self.assertIn(expected, response.data.decode('utf-8'))

if __name__=="__main__":
    unittest.main()