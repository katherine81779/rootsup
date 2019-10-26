from flask import Flask, render_template, request, redirect
app = Flask(__name__)

totalPoints = 0
username = ""


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



if __name__ == "__main__":
    app.run()