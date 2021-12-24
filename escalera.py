def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def soluciones(x):
    return fibonacci(x + 1)

if __name__ == "__main__":
    try:
        x=int(input('Número de escalones a subir'))
        print ("Cantidad de soluciones = ",soluciones(x))
    except:
        print("Valor ingresado no válido")

