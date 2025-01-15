from flask import Flask, render_template, request
from calculator import calculate  # Import your calculator function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        expression = request.form["expression"]
        result = calculate(expression)  # Call your Python calculator logic
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
