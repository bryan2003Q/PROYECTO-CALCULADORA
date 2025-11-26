from flask import Flask, render_template, request

app = Flask(__name__)

def sumar(a, b):
    return a + b

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    if b == 0:
        return "Error: No se puede dividir para cero"
    return a/b 

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    if request.method == 'POST':
        try:
            val1 = float(request.form['val1'])
            val2 = float(request.form['val2'])
            operacion = request.form.get('op')
            
            if operacion == "multiplicar":
                resultado = multiplicar(val1, val2)

            elif operacion == "restar":
                resultado = restar(val1, val2)

            elif operacion == "dividir":
                resultado = dividir(val1, val2)

            else:  # sumar por defecto
                resultado = sumar(val1, val2)
            
            
        except ValueError:
            resultado = "Error: Ingresa números válidos"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)