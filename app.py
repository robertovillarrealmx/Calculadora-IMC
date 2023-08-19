from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Código para obtener datos del formulario
        datos = {
            'nombre': request.form.get('nombre'),
            'apellido_paterno': request.form.get('apellido_paterno'),
            'apellido_materno': request.form.get('apellido_materno'),
            'edad': request.form.get('edad'),
            'peso': float(request.form.get('peso')),
            'estatura': float(request.form.get('estatura'))
        }
        
        # Código para calcular el IMC
        imc = datos['peso'] / (datos['estatura'] ** 2)
        
        # Clasificación del IMC
        if imc < 18.9:
            clasificacion = "Peso bajo"
        elif imc < 25:
            clasificacion = "Peso normal"
        elif imc < 30:
            clasificacion = "Sobrepeso"
        elif imc < 35:
            clasificacion = "Obesidad leve"
        elif imc < 40:
            clasificacion = "Obesidad media"
        else:
            clasificacion = "Obesidad mórbida"
        
        return jsonify({
            'nombre': datos['nombre'],
            'apellido_paterno': datos['apellido_paterno'],
            'apellido_materno': datos['apellido_materno'],
            'edad': datos['edad'],
            'imc': round(imc, 2),
            'clasificacion': clasificacion
        })

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
