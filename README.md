# Portafolio Módulo 3 - Fundamentos de Python

Este repositorio contiene los programas desarrollados durante el **Módulo 3** del **Bootcamp Desarrollo Full Stack Python**, enfocados en la aplicación práctica de los conceptos fundamentales del lenguaje.  
Cada programa resuelve un problema específico, utilizando estructuras, tipos de datos, funciones y control de flujo.

---

## 📌 Objetivos del módulo

- Comprender y aplicar los fundamentos de Python.  
- Desarrollar programas que utilicen variables, operadores, estructuras de control y funciones.  
- Modularizar y reutilizar código de manera eficiente.  
- Utilizar estructuras de datos como listas y diccionarios.  
- Subir el trabajo a GitHub para mantener el historial del proyecto.  

---

## 🧩 Programas desarrollados

### 1️⃣ Conversor de monedas (`1_Conversor/conversor_monedas.py`)
Convierte entre CLP, USD, EUR y CNY de manera interactiva, usando un menú en consola.  

**Conceptos aplicados:**
- Variables y operadores para cálculos de conversión.  
- Condicionales `if/elif/else` para seleccionar la operación.  
- Bucle `while` para mantener el menú hasta salir.  
- Funciones (`convertir`, `pedir_cantidad`, `mostrar_menu`).  
- Validaciones: no acepta números negativos ni entradas inválidas.  
- Historial de conversiones registrado en una lista y mostrado al finalizar.  

---

### 2️⃣ Formulario interactivo (`2_Formulario/formulario.py`)
Permite al usuario registrar información básica de forma segura y validada.  

**Características:**
- Solicita nombre, correo electrónico, edad, aceptación de términos y deseo de ser contactado.  
- Tipos de datos usados:
  - `str` para nombre y correo electrónico  
  - `int` para edad  
  - `bool` para aceptación de términos y contacto  
- Validaciones implementadas:
  - Nombre solo con letras y espacios, no vacío  
  - Correo electrónico con formato básico (`@` y `.`)  
  - Edad positiva y numérica  
  - Sí/No para respuestas booleanas  
- Manejo de errores mediante bucles y validación de entrada, evitando cierres por datos inválidos.  
- Muestra un resumen de los datos ingresados, incluyendo el nombre en el mensaje de agradecimiento.  

---

### 3️⃣ Determinar si un número es positivo, negativo o cero (`3_Numeros/numeros.py`)
Solicita un número al usuario y muestra si es **positivo**, **negativo** o **cero**.  

**Conceptos aplicados:**
- Tipos de datos numéricos (`float`).  
- Condicionales (`if`, `elif`, `else`).  
- Excepciones (`try`, `except`).  
- Bucle interactivo (`while`).  

---

### 4️⃣ Generador de Tablas y Factoriales (`4_Generador_multiplicacion/multiplicacion.py`)
Permite generar tablas de multiplicar, calcular factoriales y realizar multiplicaciones infinitas.  

**Conceptos aplicados:**
- Bucles `for` y `while` para repetir acciones.  
- Funciones y manejo de excepciones.  
- Menú interactivo en consola.  
- Uso de estructuras iterativas para resolver distintos tipos de cálculos.  

---

### 5️⃣ Agenda de Contactos (`5_Agenda_Contactos/agenda.py`)
Implementa una agenda de contactos en consola utilizando un diccionario para almacenar los datos.  

**Características:**
- Permite agregar, visualizar y validar contactos.  
- Asegura que los nombres no contengan números y que los correos y teléfonos sean válidos.  
- Demuestra el uso de estructuras de datos (`dict`), validaciones, bucles y control de flujo.  

---

### 6️⃣ Cálculo de áreas de figuras geométricas (`6_Calculadora_area/calculadora_area.py`)
Permite calcular el área de diferentes figuras geométricas (rectángulo, triángulo, círculo y cuadrado).  

**Conceptos aplicados:**
- Funciones independientes para cada figura.  
- Menú interactivo con validaciones.  
- Bucle `while` para repetir operaciones.  
- Demuestra el uso de funciones, estructuras de control y tipos numéricos en Python.  

---

## 🗃️ Estructura del repositorio

```bash
Evaluacion_Portafolio_M3/
├── 1_Conversor/
│   └── conversor_monedas.py
│
├── 2_Formulario/
│   └── formulario.py
│
├── 3_Numeros/
│   └── numeros.py
│
├── 4_Generador_multiplicacion/
│   └── multiplicacion.py
│
├── 5_Agenda_Contactos/
│   └── agenda.py
│
├── 6_Calculadora_area/
│   └── calculadora_area.py
│
└── README.md

---

## 🛠 Tecnologías utilizadas

- **Lenguaje:** Python 3  
- **Editor:** Visual Studio Code / Terminal  
- **Control de versiones:** Git y GitHub  
- **Entorno:** Consola interactiva (CLI)  

---

## Autoría

Proyecto desarrollado por **Sofía Lagos**  
📚 Bootcamp Desarrollo Full Stack Python — Módulo 3  
🌐 GitHub: [github.com/too0oori](https://github.com/too0oori)

---

