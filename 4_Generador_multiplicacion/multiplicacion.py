def tabla_multiplicar(n):
    """Muestra la tabla de multiplicar del número dado """
    print(f"\nTabla de multiplicar del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def factorial(n):
    """Calcula el factorial del número dado."""
    resultado = 1
    contador = n
    while contador > 1:
        resultado *= contador
        contador -= 1
    return resultado

def multiplicar_infinito(n):
    """Muestra multiplicaciones infinitas del número dado."""
    i = 1
    while True:
        print(f"{n} x {i} = {n * i}")
        i += 1
        continuar = input("\nPresiona Enter para continuar o escribe 'salir' para detener: ").strip().lower()
        if continuar == 'salir':
            break

def menu():
    """Muestra el menú principal y controla el flujo del programa."""
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("\n1. Tabla de multiplicar")
        print("\n2. Factorial")
        print("\n3. Multiplicación infinita")
        print("\n4. Salir")

        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            try:
                n = int(input("\nIngresa un número entero: "))
                tabla_multiplicar(n)
            except ValueError:
                print("\n❌ Entrada no válida. Ingresa un número entero.")
        elif opcion == "2":
            try:
                n = int(input("\nIngresa un número entero: "))
                if n < 0:
                    print("\n❌ No se puede calcular el factorial de un número negativo.")
                else:
                    print(f"\nEl factorial de {n} es: {factorial(n)}")
            except ValueError:
                print("\n❌ Entrada no válida. Ingresa un número entero.")
        elif opcion == "3":
            try:
                n = int(input("\nIngresa un número entero: "))
                multiplicar_infinito(n)
            except ValueError:
                print("\n❌ Entrada no válida. Ingresa un número entero.")
        elif opcion == "4":
            print("\nGracias por usar el programa. Chaooo!")
            break
        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()