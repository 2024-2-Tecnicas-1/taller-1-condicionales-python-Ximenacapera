def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    imc = peso / (estatura ** 2)
    if edad < 45: 
        if imc < 22.0:
            condicion = "bajo"
        elif imc >= 22.0:
             condicion = "medio"
    else:
        if edad >= 45:
            if imc >= 22.0:
                condicion = "alto"
            elif imc < 22.0:
                condicion = "medio"
    return condicion;

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
