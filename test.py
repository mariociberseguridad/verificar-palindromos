import unittest
from charfun import esPalindromo

"""
    Esta clase implementa un conjunto de pruebas unitarias para verificar el correcto funcionamiento de 
    la función 'esPalindromo'. Utiliza la librería 'unittest' para automatizar y estructurar los tests.

    Para los casos de prueba se han creado 3 arrays:
    
    - palindromos: array con cadenas de texto que son palíndromos válidos.

    - no_palindromos: array con cadenas de texto válidas que no son palíndromos.

    - casos_erroneos: array con entradas que deberían lanzar un error, incluyendo el tipo de excepción esperada.

    Se pueden agregar nuevos casos de prueba simplemente añadiéndolos a los arrays correspondientes en función de
    la prueba que se desee realizar. 
    
    Para automatizar los casos de prueba, se han creado 3 funciones:

    - test_palindromos: verifica que todas las entradas del array 'palindromos' sean correctamente 
    identificadas como palíndromos. Utiliza 'assertEqual' para comparar el resultado esperado.

    - test_no_palindromos: verifica que todas las entradas del array 'no_palindromos' sean correctamente 
    identificadas como no palíndromos. También utiliza 'assertEqual' para las comparaciones.

    - test_casos_erroneos: verifica que las entradas del array 'casos_erroneos' lancen la excepción esperada 
    (ya sea 'ValueError' o 'TypeError'). Utiliza 'assertRaises' para manejar las excepciones. 

"""
class Test(unittest.TestCase):
    
    # Array que guarda casos de palíndromos válidos
    palindromos = [
        "Anita lava la tina",  # Frase palíndroma
        "Roma ni se conoce sin oro, ni se conoce sin amor", # Frase palíndroma más larga
        "¡Anita! Lava     la TINA.",  # Frase palíndroma con signos de puntuación, mayúsculas y espacios
        "Oso",  # Palabra palíndroma
        "¿Acaso hubo búhos acá?",  # Frase palíndroma con signos de puntuación y tildes
    ]

    # Array que guarda cadenas de texto válidas pero que no son palíndromos
    no_palindromos = [
        "Todo ha salido a pedir de Milhouse",
        "¡Caramba!",
        "¿Inflamable significa flamable?",
        "Consiste en lanzar aros"
    ]

    # Array que guarda distintos tipos de entradas no válidas que deberían lanzar un error
    casos_erroneos = [
        ("c", ValueError),          # Solo una letra
        ("2", ValueError),          # Cadena de solo un número
        ("346", ValueError),        # Cadena de números
        ("   ", ValueError),        # Solo espacios en blanco
        ("", ValueError),           # Cadena vacía
        ("kl67op", ValueError),     # Letras y números
        ("-€&", ValueError),        # Caracteres no válidos
        ("Anita87 lava la tina", ValueError),  # Texto con números
        (67803, TypeError),         # Número entero
        (7.8, TypeError),           # Número decimal
        ([1,2,3], TypeError),       # Lista
        ({"key": "value"}, TypeError),  # Diccionario
        ((1,2,3), TypeError),       # Tupla
        (None, TypeError),          # None
        (True, TypeError),          # Booleano
    ]


    # Función que testea si una cadena es palíndroma
    def test_palindromos (self):

        for c in self.palindromos:
           self.assertEqual(esPalindromo(c), True)

    # Función que testea si una cadena no es palíndroma
    def test_no_palindromos (self):

        for c in self.no_palindromos:
           self.assertEqual(esPalindromo(c), False)

    # Función que testea si una entrada no es válida y lanza un error
    def test_casos_erroneos (self):

        for c in self.casos_erroneos:
           entrada, resultado_esperado =  c
           with self.assertRaises(resultado_esperado):
               esPalindromo(entrada)

if __name__ == "__main__":
    unittest.main()
