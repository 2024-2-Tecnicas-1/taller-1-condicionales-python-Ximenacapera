def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
     if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        return "Año bisiesto"
     else:
        return"Año no bisiesto"
     

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
