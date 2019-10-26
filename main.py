from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def redir():
    return render_template('index.html')

@app.route("/fitness")
def goToFitnessPage():
    return render_template('fitness.html')
    


if __name__ == "__main__":
    app.run()