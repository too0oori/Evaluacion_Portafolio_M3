# conversor_monedas.py

historial_conversiones = []
def convertir(moneda_origen, moneda_destino, cantidad, tasa):
    resultado = cantidad * tasa
    print(f"\n{cantidad} {moneda_origen} son {resultado:.2f} {moneda_destino}")
    print(f"Tasa de conversión: 1 {moneda_origen} = {tasa} {moneda_destino}\n")
    historial_conversiones.append(f"{cantidad} {moneda_origen} → {resultado:.2f} {moneda_destino}")

def pedir_cantidad(moneda):
    while True:
        try:
            cantidad = float(input(f"\nIngresa la cantidad en {moneda}: "))
            if cantidad <= 0:
                print("\n❌ Por favor, ingresa una cantidad positiva.")
            else:
                return cantidad
        except ValueError:
            print("\n❌ Entrada no válida. Por favor, ingresa un número.")

def conversor_monedas():
    tasas = {
        "CLP_USD": 0.0011,
        "CLP_EUR": 0.0010,
        "CLP_CNY": 0.0082,
        "USD_CLP": 920.0,
        "EUR_CLP": 1000.0,
        "CNY_CLP": 120.0
    }
    
    while True:
        try:
            mostrar_menu()
            opcion = input("\nSelecciona una opción (1-7): ")

            if opcion == "1":
                cantidad = pedir_cantidad("CLP")
                convertir("CLP", "USD", cantidad, tasas["CLP_USD"])
                input("\nPresiona Enter para volver al menú...")

            elif opcion == "2":
                cantidad = pedir_cantidad("CLP")
                convertir("CLP", "EUR", cantidad, tasas["CLP_EUR"])
                input("\nPresiona Enter para volver al menú...")

            elif opcion == "3":
                cantidad = pedir_cantidad("CLP")
                convertir("CLP", "CNY", cantidad, tasas["CLP_CNY"])
                input("\nPresiona Enter para volver al menú...")

            elif opcion == "4":
                cantidad = pedir_cantidad("USD")
                convertir("USD", "CLP", cantidad, tasas["USD_CLP"])
                input("\nPresiona Enter para volver al menú...")

            elif opcion == "5":
                cantidad = pedir_cantidad("EUR")
                convertir("EUR", "CLP", cantidad, tasas["EUR_CLP"])
                input("\nPresiona Enter para volver al menú...")

            elif opcion == "6":
                cantidad = pedir_cantidad("CNY")
                convertir("CNY", "CLP", cantidad, tasas["CNY_CLP"])

                input("\nPresiona Enter para volver al menú...")

            elif opcion == "7":
                print("\nHistorial de conversiones:")
                for registro in historial_conversiones:
                    print("\n- " + registro)
                print("\nGracias por usar el conversor de monedas, hasta pronto!!")
                break
            else:
                print("\nOpción no válida. Intenta de nuevo.")
        except ValueError:
            print("\nEntrada no válida. Por favor, ingresa un número.")


def mostrar_menu():
    print("\n==============================")
    print("     CONVERSOR DE MONEDAS     ")
    print("==============================")
    print("\nBienvenidx al conversor de monedas! \nConvierte entre CLP, USD, EUR y CNY fácilmente.\n")
    print("\n¿Qué moneda deseas convertir?")
    print("\n1. Convertir CLP a USD")
    print("2. Convertir CLP a EUR")
    print("3. Convertir CLP a CNY")
    print("4. Convertir USD a CLP")
    print("5. Convertir EUR a CLP")
    print("6. Convertir CNY a CLP")
    print("7. Salir")

if __name__ == "__main__":
    conversor_monedas()
