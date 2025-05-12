# Verificador de palíndromos en Python

Este proyecto contiene un script simple en Python para verificar si una cadena de texto introducida por el usuario es un palíndromo. También incluye pruebas unitarias para asegurar el correcto funcionamiento de la lógica principal.

## Descripción

El programa principal (`charfun.py`) solicita al usuario que ingrese una frase y luego determina si es un palíndromo (se lee igual hacia adelante que hacia atrás, ignorando espacios, tildes y caracteres no alfanuméricos).

El script de pruebas (`test.py`) utiliza el módulo `unittest` de Python para verificar la función `esPalindromo` con varios casos, incluyendo frases palíndromas, no palíndromas y casos erróneos.

## Tecnología Utilizada

* **Lenguaje:** Python 3
* **Frameworks/Librerías:**
    * `unittest` (para las pruebas unitarias, parte de la biblioteca estándar de Python)

## Instalación

No se requiere instalación adicional más allá de tener Python 3 instalado en tu sistema.

1.  Clona o descarga este repositorio.
2.  Asegúrate de tener Python 3 instalado ([https://www.python.org/](https://www.python.org/)).

## Uso

1.  **Para ejecutar el verificador de palíndromos:**
    ```bash
    python charfun.py
    ```
    El programa te pedirá que introduzcas una frase.

2.  **Para ejecutar las pruebas unitarias:**
    ```bash
     python -m unittest -v test
    ```
    Los resultados de las pruebas se mostrarán en la consola.

## Autor

* Mario

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.