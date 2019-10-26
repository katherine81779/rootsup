from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)

totalPoints = 0
username = ""

from nutritionix import Nutritionix
nix = Nutritionix(app_id="cf89e5fd", api_key="a5dbbc411a9326eb6c9391e93071677e")


@app.route("/")
def redir():
    return render_template('index.html')


@app.route("/categories")
def goToCategoriesPage():
    return render_template('categories.html', totalPoints = totalPoints)

@app.route("/diet")
def goToDietPage():
    return render_template('diet.html', totalPoints = totalPoints)

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
    if request.method == 'POST':
        foodInput = request.form['foodItem']
        nix.search(foodInput)
        results = foodInput.json()
        print(results)

        print(nix.search().nxql(fields=["nf_calories"]).json())



if __name__ == "__main__":
    app.run()