import basic_gd4 as db
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def homepage():
     '''renders html for the homepage, where the main functions are'''
     return render_template("homepage.html")

@app.route('/get_calorie', strict_slashes=False)
def get_calorie_by_food():
     '''display the calorie count of the food'''
     food = request.args['text_box']
     calorie = db.get_calories_by_name(food)
     if calorie == "Sorry, the item you are searching for is not in the menu of Chick-fil-A.":
          return render_template("foodNotFoundPage.html")
     return render_template("calorie.html", food = food, count = calorie, num_present = round(100*(calorie/600), 2))

@app.route('/get_diet', strict_slashes=False)
def get_diet():  
     '''display the dietary restriction based on food'''
     food = request.args['text_box']
     food_list = food.split(",")
     allergies = str(db.get_restriction(food_list))
     if allergies == "Sorry, the item you are searching for is not in the menu of Chick-fil-A.":
          return render_template("foodNotFoundPage.html")
     return render_template("diet.html", food = food, allergies = allergies[1:-1])

@app.route('/about')
def aboutpage():
     '''renders html for the about page'''
     return render_template("about.html")

@app.route('/contact')
def contactpage():
     '''renders html for the contact page'''
     return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
     '''error handling for 404 error (URL not found)'''
     return render_template("errorpage.html")

@app.errorhandler(500)
def python_bug(e):
     '''error handling for 500 error'''
     return "Internal Server Error"



if __name__ == '__main__':
    app.run(port = 5001)