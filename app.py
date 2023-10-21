from flask import Flask, render_template
from ProductionCode.basic_cl import *

app = Flask(__name__)


def calories_message(result, food):
     '''Helper function: process and return a corresponding message for get_calorie based on the result(found/not found)'''
     if (result == "Sorry, the item you are searching for is not in the menu of Chick-fil-A."):
          return result
     else:
          msg_pt1 = "Calorie count of "
          return msg_pt1 + food + " is " + str(result) + "."


def diet_message(result):
     '''Helper function: process and return a corresponding message for get_allergies based on the result(found/not found)'''
     if (result == "Sorry, the item you are searching for is not in the menu of Chick-fil-A."):
          return result
     elif(len(result)==0):
          no_allergy_msg = "Your food include(s) no allergies. Have fun!"
          return  no_allergy_msg
     else:
          msg_pt1 = "Your food include(s) "
          return msg_pt1 + (str(result))[1:-1]+ ". Pay attention!"

def split_food_input(food):
     return food.split(",")


@app.route('/')
def homepage():
     '''display usage statement on the homepage'''
     calories_instruction  = "To get calories by food name: access http://XXX.X.X.X:YYYY/calorie/food"
     return render_template("homepage_old.html")

@app.route('/calorie/<food>', strict_slashes=False)
def get_calorie(food = ""):
     '''display the calorie count of the food item, if food item not found, then display a message'''
     load_data()
     result = get_calories_by_name(food)
     message = calories_message(result, food)
     return render_template("calorie.html", message = message)


@app.route('/diet/<food>', strict_slashes=False)
def get_allergies(food = ""):
     '''display the allergies of the food item, if food item not found, then display a message'''
     food_list = split_food_input(food)
     load_data()
     result = get_restriction(food_list)
     message = diet_message(result) 
     return render_template("diet.html", message = message)


@app.errorhandler(404)
def page_not_found(e):
     '''error handling for 404 error (URL not found)'''
     err_msg = "Oops, the page you were looking for doesn't exist, please refer to homepage or go to one of the pages below:"
     return render_template("error_page.html")


@app.errorhandler(500)
def python_bug(e):
     '''error handling for 500 error'''
     return "Internal Server Error"

if __name__ == '__main__':
    app.run()