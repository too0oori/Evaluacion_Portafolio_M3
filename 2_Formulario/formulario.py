#formulario.py

def seleccion(pregunta):
    """
    Solicita una respuesta sí/no al usuario y devuelve True o False.
    """
    while True:
        respuesta = input(pregunta + " (s/n): ").strip().lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False
        else:
            print("\n❌ Entrada no válida. Por favor, ingresa 's' para sí o 'n' para no.")

def solicitar_entero(pregunta):
    """
    Solicita un número entero al usuario y maneja errores de entrada.
    """
    while True:
        try:
            valor = int(input(pregunta + ": ").strip())
            if valor <= 0:
                print("\n❌ Por favor, ingresa un número entero positivo.")
            else:
                return valor
        except ValueError:
            print("\n❌ Entrada no válida. Por favor, ingresa un número entero.")

def solicitar_nombre(pregunta):
    while True:
        nombre = input(pregunta + ": ").strip()
        if nombre == "":
            print("\n❌ El nombre no puede estar vacío.")
        elif not all(c.isalpha() or c.isspace() for c in nombre):
            print("\n❌ El nombre solo puede contener letras y espacios.")
        else:
            return nombre


def solicitar_email(pregunta):
    """
    Solicita un correo electrónico al usuario y verifica que tenga un formato básico.
    """
    while True:
        email = input(pregunta + ": ").strip()
        if "@" in email and "." in email:
            return email
        else:
            print("\n❌ Por favor, ingresa un correo electrónico válido.")

def formulario():
    print("\nBienvenidx al formulario de registro.")
    nombre = solicitar_nombre("\nPor favor, ingresa tu nombre")
    email = solicitar_email("\nPor favor, ingresa tu correo electrónico")
    edad = solicitar_entero("\nPor favor, ingresa tu edad")
    acepta_terminos = seleccion("\n¿Aceptas los términos y condiciones?")
    contacto = seleccion("\n¿Deseas ser contactadx?")

    print("\nGracias por completar el formulario, {nombre}!".format(nombre=nombre))
    print(f"\nNombre: {nombre}")
    print(f"\nCorreo Electrónico: {email}")
    print(f"\nAcepta Términos y Condiciones: {'Sí' if acepta_terminos else 'No'}")
    print(f"\nEdad: {edad}")
    print(f"\nDesea ser contactadx: {'Sí' if contacto else 'No'}")
    input("\nPresiona Enter para volver al menú...")

if __name__ == "__main__":
    formulario()