"""
    La función 'esPalindromo' recibe una cadena de texto y determina si es un palíndromo. Ignora espacios, 
    tildes y caracteres no alfabéticos.

    Paramétros:
    cadena (str): La cadena que será evaluada como posible palíndromo.

    Retorno:
    bool: Devuelve True si la cadena es un palíndromo y False si no.

    Excepciones:
    ValueError: Si la cadena contiene números o caracteres no alfabéticos.
    TypeError: Si el tipo de dato de la cadena no es una cadena de texto.

"""
def esPalindromo(cadena):

    # Verificamos que la entrada sea una cadena, si no lo es, lanzamos un error
    if not isinstance(cadena, str):
        raise TypeError("La entrada debe ser una cadena de texto.")

    # Convertimos la cadena a minúsculas, eliminamos espacios en blanco y quitamos las tildes
    cadena = cadena.lower().replace(' ', '').replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")

    # Verificamos si la entrada contiene algún número, en ese caso, lanzamos un error
    if any(c.isdigit() for c in cadena):
        raise ValueError("La entrada no puede contener números.")

    # Construimos la cadena introducida pero solo con letras
    cadena_solo_letras = "".join(c for c in cadena if c.isalpha())

    # Si se introduce sólo una letra, lanzamos un error, al menos se deben introducir dos letras
    if len(cadena_solo_letras) < 2:
        raise ValueError("La entrada debe contener al menos dos letras.")

    # Verificamos si la cadena ya limpiada es igual a su reverso. Devolverá True si es igual a su reverso o False si no
    return cadena_solo_letras == cadena_solo_letras[::-1]

"""
    La función main es el punto de entrada principal del programa. Solicita al usuario una frase o palabra e 
    invoca la función 'esPalindromo' para determinar si la entrada es un palíndromo o no. 

    El programa ejecuta un bucle que permite al usuario ingresar múltiples frases, mostrando el resultado 
    para cada una de ellas hasta que el usuario introduce 's' para salir del programa.

"""
def main():

    while True:

        try:
            # Solicitamos al usuario que introduzca una frase por teclado.
            cadena = input("Introduce una frase o una palabra de al menos 2 letras (Escribe 's' para salir del programa): ")

            # Comprobamos primero si el usuario ha introducido la letra 's' para salir del programa
            if cadena.lower() == 's':
                print("Programa finalizado")
                break

            # Verificamos si la cadena introducida es palíndroma
            if esPalindromo(cadena):
                print("La frase es un palíndromo.")
            else:
                print("La frase no es un palíndromo.")

        # Gestionamos los posibles errores
        except ValueError:
            print("Error. Se ha introducido un dato no válido. Debe introducir 2 o más letras.")
        
        except TypeError:
            print("Error. Se ha introducido un tipo de dato no válido. Sólo se permiten cadenas de texto.")
        
        except Exception:
            print("Error inesperado. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
