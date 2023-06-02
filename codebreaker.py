""" Clase Codebreaker.

    Define método que implementa la lógica del juego.

    Recibe un número, lo valida y verifica si el número recibido es igual al
    número que se el jugador debe adinivnar, establecido a través de la
    constante NUMERO_CORRECTO.

    Si el número recibido es correcto pero no igual al NUMERO_CORRECTO,
    se ejecuta la lógica que determinará cuantos números se han acertado y si
    su posición coincide con la del NUMERO_CORRECTO.
"""


NUMERO_CORRECTO = "1010"


class Codebreaker:

    def adivinar(self, numero=None):
        if NUMERO_CORRECTO == '':
            return 'El número a adivinar no ha sido asignado'

        if numero is None or len(numero) != 4 or numero.isalpha():
            return "Error"

        if numero == NUMERO_CORRECTO:
            return True

        resultado_ = ''  # Almacena coincidencias de cifra pero no de posición
        resultado_x = ''  # Almacena coincidencia de cifra y posición

        numero = list(numero)

        """
         Recorro el número recibido comprobando coincidencias de cifra
         y posición
        """

        for index, cifra in enumerate(numero):
            if NUMERO_CORRECTO[index] == cifra:
                resultado_x += 'X'
            elif cifra in NUMERO_CORRECTO:
                resultado_ = '_'

        return resultado_x + resultado_
