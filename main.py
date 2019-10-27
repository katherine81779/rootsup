from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)

totalPoints = 0
username = ""
calories = 2000

from nutritionix import Nutritionix
nix = Nutritionix(app_id="cf89e5fd", api_key="a5dbbc411a9326eb6c9391e93071677e")


@app.route("/")
def redir():
    return render_template('index.html')


@app.route("/categories")
def goToCategoriesPage():
    return render_template('categories.html', totalPoints = totalPoints, calories = calories)

@app.route("/diet")
def goToDietPage():
    return render_template('diet.html', totalPoints = totalPoints, calories = calories)

@app.route("/fitness")
def goToFitnessPage():
    return render_template('fitness.html', totalPoints = totalPoints)

@app.route("/sleep")
def goToSleepPage():
    return render_template('sleep.html', totalPoints = totalPoints)

@app.route("/inputSleep", methods = ['POST', 'GET'])
def enterHours():
    global totalPoints

    if request.method == 'POST':
        hours = request.form['hours']
        points = int(hours) * 10
        totalPoints += points

        return redirect("/categories")

@app.route("/inputFood", methods = ['POST', 'GET'])
def enterFood():
    global totalPoints
    global calories

    if request.method == 'POST':
        foodInput = request.form['foodItem']

        if foodInput.split()[0] == "ADD":
            calories += int(foodInput.split()[1])

        else:
            food = nix.search(foodInput, results="0:1")
            results = food.json()

            foodID = results[u'hits'][0][u'_id']
            item = nix.item(id=foodID).json()
            foodCalories = item[u'nf_calories']

            calories -= foodCalories
            if calories < 0:
                totalPoints -= 100
                
        return redirect("/diet")



if __name__ == "__main__":
    app.run()