def evaluar(a, b):
    #TODO: Coloca aquí el código del ejercicio 1: Set de tenis

    if (a < 0 or b < 0) or (a > 7 or b > 7) or (a == 7 and b == 7):
        return "Inválido"
    
    if a >= 6 and a >= b + 2:
        return "Ganó A"
    
    if b >= 6 and b >= a + 2:
        return "Ganó B"
    
    if (a == 7 and b == 6 ): 
        return "Ganó A" 
    
    elif (b == 7 and a == 6):
        return "Ganó B"
    return "Aún no termina"

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
