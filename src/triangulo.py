def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
   
    if a + b > c and a + c > b and b + c > a:
        if a == b == c: 
            return "El triángulo es equilatero"
        elif a == b or b == c or a == c: 
            return "El triángulo es isóceles"
        else:
            return "El triángulo es escaleno"
    else:
        return "No es un triángulo válido"

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
