# Mi Movistar

Este repositorio muestra mis primeros pasos en programación con python. Son distintos proyectos realizados por día durante una parte del módulo de python.

# Índice

1. [Estado del Proyecto](#id1)
2. [Descripción del Proyecto](#id2)
3. [Tecnologías Utilizadas](#id3)
4. [Estructura del proyecto](#id4)
5. [Características](#id5)
6. [Diseño](#id6)
7. [Instrucciones](#id7)
8. [Personas Desarrolladoras del Proyecto](#id8)

# Estado del proyecto<a name="id1"></a>

Finalizado

# Descripción del Proyecto<a name="id2"></a>

Son once carpetas las que hacen parte de este repositorio, cada una con diferentes ejercicios matemáticos, lógicos y algunos conceptos importantes del lenguaje. Los ejercicios son: 

1. Dia 1
- main.py: Este archivo contiene ejemplos de los tipos de datos primitivos python. Además, se realizan varios procedimientos en el mismo código: hacer una entrada se usuario, convertir tipos de variables, creación de bucles while y for y creación de funciones.

2. Dia 2
- adivinar.py: Este es un juego interactivo. El objetivo es adivinar un número secreto generado aleatoriamente entre 1 y 100. Después de cada intento, recibirás una pista para ayudarte a acercarte al número correcto.

-**Cómo jugar**
Ejecuta el programa.
Se generará un número secreto aleatorio.
Ingresa tu suposición (debe estar entre 1 y 100).
Recibirás retroalimentación sobre si tu suposición es demasiado alta o demasiado baja.
Continúa adivinando hasta que aciertes o hayas realizado 10 intentos.

- fibonacci.py: Este programa escrito en Python genera la famosa secuencia de Fibonacci hasta un término especificado por el usuario. Pero, ¿qué es la secuencia de Fibonacci?. La secuencia de Fibonacci es una serie matemática en la que cada número es la suma de los dos anteriores. Comienza con los números 0 y 1, y luego cada término subsiguiente se calcula como la suma de los dos términos anteriores. Así que la secuencia comienza así: 0, 1, 1, 2, 3, 5, 8, 13, …

-**Cómo usar este programa**
Ejecuta el programa.
Ingresa un número entero que represente hasta qué término de la secuencia deseas generar.
El programa imprimirá la secuencia de Fibonacci hasta ese término.
Puedes repetir el proceso o finalizar el programa según tu preferencia.

- intentosinf.py: En este juego interactivo, tendrás que adivinar un número secreto. Después de cada intento, recibirás retroalimentación para ayudarte a acercarte al número correcto. Lo que lo diferencia de **adivinar.py** es que este tiene intentos infinitos.

-**Cómo jugar**
Ejecuta el programa.
Se generará un número secreto aleatorio entre 1 y 100.
Ingresa tu suposición (debe estar entre 1 y 100).
Recibirás pistas como “Demasiado bajo” o “Demasiado alto” según tu suposición.
Continúa adivinando hasta que aciertes o hayas realizado varios intentos.

3. Dia 3
- primo.py: Este archivo realiza dos procedimientos. Puedes verificar si un número es primo ingresandolo en una entrada de texto, y generar una contraseña segura, escogiendo los caracteres que quieres que tenga la contraseña (longitud, minusculas, mayusculas, numeros, especiales)

4. Dia 4
- cambio.py: Este programa indica el cambio de dinero que se debe dar a un cliente con la cantidad minima de modedas posibles de denominaciones: 1, 5, 10. Solo ingresas la cambio y el programa te devolverá el valor del cambio.

5. Dia 5
- ejercicio1.py: Se hace uso de una función parejas(a, n, k), verifica los pares de números en una lista a de longitud n y determina cuántos de estos pares tienen una suma divisible por un número dado k

6. Dia 6
- enumerador.py: La función duplicados(nums, destino) busca un par de números en una lista nums cuya suma sea igual a un valor objetivo (destino). Aquí están los detalles: 

-La función crea un diccionario llamado indices para almacenar los números y sus índices en la lista.

-Luego, recorre la lista de números y calcula el complemento necesario para alcanzar el objetivo.

-Si el complemento está en el diccionario, se ha encontrado un par válido, y la función devuelve los índices de esos números.

-Si no se encuentra ningún par, se devuelve un mensaje indicando que no se encontró solución.

- nodos.py: El Eliminador de Duplicados es un programa en Python que toma una lista de valores y devuelve una versión ordenada de la lista sin elementos duplicados. El usuario ingresa unos valores en un rango entre 0 y 300 y los dupliacdos son eliminados.

7. Dia 7
- grupo.py: Programa para concesionario, se pueden realizar compras y agregar a carritos.

8. Dia 8
- fruticas.py: Carrito de compras
- suscripcion.py: 

9. Dia 9
- carrito.py

10. Dia 10
- posicion.py:

11. Dia 11
- jsonj.py:
- repaso.py:

# Tecnologías utilizadas<a name="id3"></a>

* Python

# Estructura del proyecto<a name="id4"></a>

![alt text](<Captura de pantalla 2024-08-05 213829.png>)
![alt text](<Captura de pantalla 2024-08-05 213855.png>)

# Características<a name="id5"></a>

Archivos Fundamentales:

**movistar.py**: Este archivo es el corazón del sistema. Contiene el código que maneja la parte lógica del programa, es fundamental para que funcione el sistema.

**categoriasUsuarios.json**: Aquí se guarda la información de los clientes de acuerdo a su categoría, que pueden ser nuevos clientes, clientes regulares o clientes leales.

**registro.json**: Aquí se guarda la información de cada cliente, dada por ellos mismos al momento del registro a la plataforma.

**servicios.json**: Aquí se guarda la información de cada servicio (características y precio) que ofrece la empresa. Además, cada servicio ofrece la información de los clientes que lo han adquirido.

# Diseño<a name="id6"></a>

* Solo puede ser visto y usado en consola

# Instrucciones<a name="id7"></a>

1. Clonar el repositorio
~~~
https://github.com/JesusBustamante/python_BustamanteJesus.git
~~~

2. Si es clonado en Visual Studio Code, descargue la extensión de Python.

3. También descargue python desde un navegador web o la microsoft store.

3. Ejecuta el programa en la terminal de GitBash de la siguiente forma: 
~~~ 
python "nombredelarchivo.py"
~~~

# Personas Desarrolladoras del Proyecto<a name="id8"></a>

Este proyecto fue desarrollado por Jesús Leonardo Bustamante Ramírez, estudiante de Campuslands como parte de los proyectos requeridos para el módulo de python.