def solicitar_datos():
    """
    Solicita al usuario su nombre, apellido paterno, apellido materno, edad, peso y estatura.
    Retorna estos datos en un diccionario.
    """
    nombre = input("Introduce tu nombre: ").strip()
    apellido_paterno = input("Introduce tu apellido paterno: ").strip()
    apellido_materno = input("Introduce tu apellido materno: ").strip()
    edad = input("Introduce tu edad: ").strip()
    peso = input("Introduce tu peso en kg: ").strip()
    estatura = input("Introduce tu estatura en metros: ").strip()
    
    return {
        "nombre": nombre,
        "apellido_paterno": apellido_paterno,
        "apellido_materno": apellido_materno,
        "edad": edad,
        "peso": peso,
        "estatura": estatura
    }

def validar_datos(datos):
    """
    Valida los datos del usuario:
    - Asegura que ningún campo esté vacío.
    - Verifica que edad, peso y estatura sean cifras válidas.
    Retorna un mensaje de error si hay un problema, o None si todo está bien.
    """
    if not all(datos.values()):
        return "Ningún campo puede estar vacío."

    try:
        int(datos["edad"])
    except ValueError:
        return "La edad debe ser un número entero."

    try:
        float(datos["peso"])
    except ValueError:
        return "El peso debe ser una cifra."

    try:
        float(datos["estatura"])
    except ValueError:
        return "La estatura debe ser una cifra."

    return None

def clasificar_imc(imc):
    """
    Clasifica el IMC del usuario según los rangos especificados por el ISSSTE.
    Retorna una cadena de texto con la clasificación.
    """
    if imc < 18.9:
        return "Peso bajo"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad leve"
    elif imc < 40:
        return "Obesidad media"
    else:
        return "Obesidad mórbida"

def main_optimizado():
    """
    Función principal que coordina la ejecución del programa.
    """
    print("Calculadora de Índice de Masa Corporal (IMC)\n")
    
    datos = solicitar_datos()
    
    # Validar datos
    error = validar_datos(datos)
    if error:
        print(f"\nError: {error}")
        return

    edad = int(datos["edad"])
    peso = float(datos["peso"])
    estatura = float(datos["estatura"])

    # Calcular IMC
    imc = peso / (estatura ** 2)
    
    # Mostrar datos
    print(f"\nDatos de {datos['nombre']} {datos['apellido_paterno']} {datos['apellido_materno']}:")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
    print(clasificar_imc(imc))

# La función se ejecutaría en un entorno real llamando a main_optimizado().
# Por ahora, solo se muestra el código.

"Función 'main_optimizado' creada y lista para ser ejecutada."

if __name__ == "__main__":
    main_optimizado()
