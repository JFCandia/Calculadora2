from flask import Flask, request, render_template, session
import math

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesion'

# Función para guardar solo la nueva operación en el archivo
def guardar_historial_en_archivo(item):
    with open("historial_operaciones.txt", "a", encoding="utf-8") as archivo:
        archivo.write(item + "\n")

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    if 'history' not in session:
        session['history'] = []  # Inicializamos el historial en la sesión

    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form.get('num2', 0))  # Por defecto 0 si no se usa
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            operacion = f"{num1} + {num2} = {result}"
        elif operation == 'subtract':
            result = num1 - num2
            operacion = f"{num1} - {num2} = {result}"
        elif operation == 'multiply':
            result = num1 * num2
            operacion = f"{num1} * {num2} = {result}"
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
                operacion = f"{num1} / {num2} = {result}"
            else:
                result = "Error: División por cero"
                operacion = f"Error en división de {num1} / {num2}"
        elif operation == 'modulo':
            if num2 != 0:
                result = num1 % num2
                operacion = f"{num1} % {num2} = {result}"
            else:
                result = "Error: División por cero"
                operacion = f"Error en módulo de {num1} % {num2}"
        elif operation == 'power':
            result = num1 ** num2
            operacion = f"{num1} ^ {num2} = {result}"
        elif operation == 'sqrt':
            if num1 >= 0:
                result = math.sqrt(num1)
                operacion = f"√{num1} = {result}"
            else:
                result = "Error: Número negativo"
                operacion = f"Error en raíz cuadrada de {num1}"
        elif operation == 'factorial':
            if num1 >= 0 and num1 == int(num1):
                result = math.factorial(int(num1))
                operacion = f"{int(num1)}! = {result}"
            else:
                result = "Error: Factorial solo para enteros no negativos"
                operacion = f"Error en factorial de {num1}"

        # Agregar la operación al historial de sesión
        if result != None:
            session['history'].append(operacion)
            guardar_historial_en_archivo(operacion)  # Guardar solo la nueva operación

    return render_template('calculator.html', result=result, history=session['history'])

if __name__ == '__main__':
    app.run(debug=True)
