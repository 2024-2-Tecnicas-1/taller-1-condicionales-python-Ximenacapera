def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    ascci = ord(caracter)
    if 65 <= ascci <= 90:
        return "Es letra mayúscula"
    elif 97 <= ascci <= 122:
        return "Es letra minúscula"
    elif 48 <= ascci <= 57:
        return "Es número"
    else:
        return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
