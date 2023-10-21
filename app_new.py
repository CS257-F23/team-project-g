import ProductionCode.basic_cl as cl
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def homepage():
     '''renders html for the homepage'''
     return render_template("homepage.html")

@app.route('/get_calorie', strict_slashes=False)
def get_calorie_by_food():
     '''display the calorie count of the food'''
     cl.load_data()
     food = request.args['food_item']
     calorie = int(cl.get_calories_by_name(food))
     return render_template("calorie_page.html", food = food, count = calorie)

@app.route('/get_diet', strict_slashes=False)
def get_diet():
     cl.load_data()
     '''display the dietary restriction based on food'''
     food = request.args['food_item']
     food_list = food.split(",")
     allergies = str(cl.get_restriction(food_list))
     return render_template("diet_page.html", food = food, allergies = allergies)

@app.errorhandler(404)
def page_not_found(e):
     '''error handling for 404 error (URL not found)'''
     return render_template("404.html")

@app.errorhandler(500)
def python_bug(e):
     '''error handling for 500 error'''
     return "Internal Server Error"

if __name__ == '__main__':
    app.run()