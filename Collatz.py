#Christian Orduz Codigo: 2152104
def secuencia_collatz(n):
    secuencia = []
    while n != 1:
        secuencia.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
    secuencia.append(1)
    return secuencia

#def main():
def code():
    ultimo_digito= 4
    print (ultimo_digito)
    dig= ultimo_digito+3
    numeros = []

    for _ in range(dig):
        numero = int(input("Ingrese un número entero: "))
        numeros.append(numero)
    promedio = int(sum(numeros) / len(numeros))
    print("El promedio es: "+str(promedio))
    #En variable promedio python redondea automaticamente hacia abajo al truncarse con int
    collatz=secuencia_collatz(promedio)
    print(f"Secuencia de Collatz para el promedio ({promedio}):")
    print(collatz)
code()
