#Un programa que determine si un número es positivo, negativo o cero.

def determinar_numero():
    print("\nBienvenidx al programa para determinar si un número es positivo, negativo o cero.")
    while True:
        try:
            numero = float(input("\nIngresa un número: "))
            if numero > 0:
                print(f"\nEl número {numero} es positivo.")
            elif numero < 0:
                print(f"\nEl número {numero} es negativo.")
            else:
                print("\nEl número es cero.")
            
            print("\nPresiona Enter para ingresar otro número o escribe 'salir' para terminar.")
            respuesta = input().strip().lower()
            if respuesta == 'salir':
                print("\nGracias por usar el programa. ¡Hasta luego!")
                break
            else:
                continue
        except ValueError:
            print("\n❌ Entrada no válida. Por favor, ingresa un número.")

if __name__ == "__main__":
    determinar_numero()