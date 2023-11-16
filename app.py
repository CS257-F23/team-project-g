import ProductionCode.core_function as core
from flask import Flask, render_template, request


app = Flask(__name__)
control = core.Controller()

@app.route('/')
def homepage():
     '''renders html for the homepage, where the main functions are'''
     return render_template("homepage.html")

@app.route('/get_calorie', strict_slashes=False)
def get_calorie_by_food():
     '''display the calorie count of the food'''
     food = request.args['text_box']
     calorie = control.get_calories_by_name(food)
     if type(calorie) is bool and calorie == False:
          return render_template("foodNotFoundPage.html")
     return render_template("calorie.html", food = food, count = calorie, num_present = round(100*(calorie/600), 2))

@app.route('/get_diet', strict_slashes=False)
def get_diet():
     '''display the dietary restriction based on food'''
     food = request.args['text_box']
     food_list = food.split(",")
     allergies = control.get_restriction(food_list)
     if allergies == False:
          return render_template("foodNotFoundPage.html")
     return render_template("diet.html", food = food, allergies = allergies)

@app.route('/about')
def aboutpage():
     '''renders html for the about page'''
     return render_template("about.html")

@app.route('/contact')
def contactpage():
     '''renders html for the contact page'''
     return render_template("contact.html")

@app.route('/menu')
def menupage():
     '''displays all the food in the database that the users can search for'''
     food_list = control.get_food_list()
     return render_template("menu.html", food_list = food_list)

@app.errorhandler(404)
def page_not_found(e):
     '''error handling for 404 error (URL not found)'''
     return render_template("errorpage.html")

@app.errorhandler(500)
def python_bug(e):
     '''error handling for 500 error'''
     return "Internal Server Error"



if __name__ == '__main__':
    app.run(port = 5221, debug = False, host = '0.0.0.0')