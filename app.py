from flask import Flask, render_template
from ProductionCode.basic_cl import *

app = Flask(__name__)
usage_diet = ("Usage : python3 Production/basic_cl.py -diet 'food1' ['food2' ... ]\n"
            "Note: at least one food option is required after '-diet', multiple food items are valid as well")
data = []

def calories_message(result, food):
     '''process and return a corresponding message based on the result(found/not found)'''
     if (result == "Sorry, the item you are searching for is not in the menu of Chick-fil-A."):
          return result
     else:
          msg_pt1 = "Calorie count of "
          return msg_pt1 + food + " is " + str(result) + "."

def diet_message(result):
     if (result == "Sorry, the item you are searching for is not in the menu of Chick-fil-A."):
          return result
     elif(len(result)==0):
          no_allergy_msg = "Your food include(s) no allergies. Have fun!"
          return  no_allergy_msg
     else:
          msg_pt1 = "Your food include(s) "
          return msg_pt1 + (str(result))[1:-1]+ ". Pay attention!"

@app.route('/')
def homepage():
     '''display usage statement on the homepage'''
     calories_instruction  = "To get calories by food name: access "
     path1 = "http://XXX.X.X.X:YYYY/calorie/food"
     URL_instruction = ("Replace 'food' with the food of your choice,"
                        "'XXX.X.X.X' with your IP address, and"
                        "'YYYY' with your port number")
     
     diet_instruction  = "To get restrictions by food name: access "
     path2 = "http://XXX.X.X.X:YYYY/diet/food"
     example1 = "Usage example: http://127.0.0.1:5000/calorie/Garden Herb Ranch Sauce"
     example2 = "Usage example: http://127.0.0.1:5000/diet/Garden Herb Ranch Sauce"
     return render_template("homepage.html", usage_message_ln1 = calories_instruction+path1, usage_message_ln2 = diet_instruction+path2, 
                            usage_message_ln3 = URL_instruction, example1 = example1, example2=example2)

@app.route('/calorie/<food>', strict_slashes=False)
def get_calorie(food = ""):
     '''display the calorie count of the food item, if food item not found, then display a message'''
     load_data() #load data
     result = get_calories_by_name(food)
     message = calories_message(result, food)  #process the message based on result
     return render_template("calorie.html", message = message) 






@app.route('/diet/<food>', strict_slashes=False)
def get_allergies(food = ""):
     food_list = food.split(",")
     load_data()
     result = get_restriction(food_list)
     message = diet_message(result)  #process the message based on result
     return render_template("diet.html", message = message) 





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