from flask import Flask, request, render_template
import math  # Importamos math para operaciones matemáticas

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2 if num2 != 0 else "Error: División por cero"   
    return render_template("calculator.html", result=result)

# Asegúrate de que esta parte esté al nivel principal
if __name__ == "__main__":
    app.run(debug=True)





