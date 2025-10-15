# Un sistema de agenda de contactos con almacenamiento en un diccionario.

def solicitar_nombre(pregunta):
    while True:
        nombre = input(pregunta + ": ").strip()
        if nombre == "":
            print("\n❌ El nombre no puede estar vacío.")
        elif not all(c.isalpha() or c.isspace() for c in nombre):
            print("\n❌ El nombre solo puede contener letras y espacios.")
        else:
            return nombre

def solicitar_telefono():
    while True:
        telefono = input("Ingresa el número de teléfono (solo dígitos): ").strip()
        if telefono == "":
            print("\n❌ El número de teléfono no puede estar vacío.")
        elif not telefono.isdigit():
            print("\n❌ El número de teléfono solo puede contener dígitos.")
        else:
            return telefono

def solicitar_email():
    while True:
        email = input("Ingresa el correo electrónico: ").strip()
        if email == "":
            print("\n❌ El correo electrónico no puede estar vacío.")
        elif "@" not in email or "." not in email:
            print("\n❌ El correo electrónico no es válido.")
        else:
            return email
def mostrar_contactos(contactos):
    if not contactos:
        print("\nNo hay contactos en la agenda.")
    else:
        print("\nContactos en la agenda:")
        for nombre, info in contactos.items():
            print(f"\nNombre: {nombre}")
            print(f"Teléfono: {info['telefono']}")
            print(f"Email: {info['email']}")

def agenda_contactos():
    contactos = {}
    print("\nBienvenidx a la agenda de contactos.")
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("\n1. Agregar contacto")
        print("\n2. Ver contactos")
        print("\n3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ").strip()
        
        if opcion == "1":
            nombre = solicitar_nombre("\nIngresa el nombre del contacto")
            telefono = solicitar_telefono()
            email = solicitar_email()
            contactos[nombre] = {"telefono": telefono, "email": email}
            print(f"\n✅ Contacto '{nombre}' agregado exitosamente.")
        
        elif opcion == "2":
            mostrar_contactos(contactos)
        
        elif opcion == "3":
            print("\nGracias por usar la agenda de contactos, hasta pronto!!")
            break
        
        else:
            print("\n❌ Opción no válida. Intenta nuevamente.")
        input("\nPresiona Enter para volver al menú...")

if __name__ == "__main__":
    agenda_contactos()
    