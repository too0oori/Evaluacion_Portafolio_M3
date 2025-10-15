""" Calcular el área de diferentes figuras geométricas utilizando funciones separadas. """

def solicitar_valor(mensaje):
    """
    Solicita un número positivo al usuario.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("\n❌ El valor debe ser un número positivo.")
            else:
                return valor
        except ValueError:
            print("\n❌ Entrada no válida. Por favor, ingresa un número.")

def area_rectangulo(lado1, lado2):
    return lado1 * lado2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return 3.14159 * (radio ** 2)

def area_cuadrado(lado):
    return lado ** 2

def pausar():
    input("\n--- Presiona Enter para continuar ---\n")

def menu_figuras():
    print("\n=====================")
    print("=== Bienvenidx al programa de cálculo de Áreas ===\n")
    print("=====================")
    print("\nSelecciona una figura:")
    print("\n=== FIGURAS ===\n")
    print("1 - Rectángulo")
    print("2 - Triángulo")
    print("3 - Círculo")
    print("4 - Cuadrado")
    print("5 - Salir")
    print("\n=====================\n")

def main_figuras():
    while True:
        menu_figuras()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            lado1 = solicitar_valor("Ingrese el lado 1: ")
            lado2 = solicitar_valor("Ingrese el lado 2: ")
            print(f"\nEl área del rectángulo es: {area_rectangulo(lado1, lado2)}")
            pausar()

        elif opcion == "2":
            base = solicitar_valor("Ingrese la base: ")
            altura = solicitar_valor("Ingrese la altura: ")
            print(f"\nEl área del triángulo es: {area_triangulo(base, altura)}")
            pausar()

        elif opcion == "3":
            radio = solicitar_valor("Ingrese el radio: ")
            print(f"\nEl área del círculo es: {area_circulo(radio)}")
            pausar()

        elif opcion == "4":
            lado = solicitar_valor("Ingrese la longitud de un lado: ")
            print(f"\nEl área del cuadrado es: {area_cuadrado(lado)}")
            pausar()

        elif opcion == "5":
            print("\nGracias por usar el programa. ¡Hasta pronto!")
            break

        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")
            pausar()

if __name__ == "__main__":
    main_figuras()
