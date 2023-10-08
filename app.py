from flask import Flask, render_template
from ProductionCode.basic_cl import *

app = Flask(__name__)

data = []

def message_by_result(result, food):
     '''process and return a corresponding message based on the result(found/not found)'''
     if (result == "Sorry, the item you are searching for is not in the menu of Chick-fil-A."):
          return result
     else:
          msg_pt1 = "Calorie count of "
          return msg_pt1 + food + " is " + str(result) + "."

@app.route('/')
def homepage():
     '''display usage statement on the homepage'''
     instruction  = "To get calories by food name: access "
     path = "http://XXX.X.X.X:YYYY/calorie/food"
     instruction_pt2 = ("Replace 'food' with the food of your choice,"
                        "'XXX.X.X.X' with your IP address, and"
                        "'YYYY' with your port number")
     example = "Usage example: http://127.0.0.1:5000/calorie/Garden Herb Ranch Sauce"
     return render_template("homepage.html", usage_message_ln1 = instruction+path, usage_message_ln2 = instruction_pt2, example = example)

@app.route('/calorie/<food>', strict_slashes=False)
def get_calorie(food = ""):
     '''display the calorie count of the food item, if food item not found, then display a message'''
     load_data() #load data
     result = get_calories_by_name(food)
     message = message_by_result(result, food)  #process the message based on result
     return render_template("calorie.html", message = message) 

@app.errorhandler(404)
def page_not_found(e):
     '''error handling for 404 error (URL not found)'''
     return "sorry, wrong format, refer to the homepage for more info"

@app.errorhandler(500)
def python_bug(e):
     '''error handling for 500 error'''
     return "Internal Server Error"

if __name__ == '__main__':
    app.run()