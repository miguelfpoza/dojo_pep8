""" Entrada al juego CodeBreaker.

    Establece mediante la constante INTENTOS_TOTALES el número de intentos
    máximos que tiene el jugador para adivinar un número.

    A continuación pide al jugador que introduzca un número.

    Se llama al método 'adivinar' de la clase 'Codebreaker', encargado de 
    verificar el número introducido por el jugador.

    La lógica se repite hasta que el jugador introduzca el número correcto o 
    se supere el número de intentos.
"""


from codebreaker import Codebreaker

INTENTOS_TOTALES = 10

codebreaker = Codebreaker()

intento = 0

print('Vamos a Jugar Codebreaker!')

while intento != INTENTOS_TOTALES:
    numero = input('Numero:')

    solucion = codebreaker.adivinar(numero)

    if solucion is True:
        print('Has ganado!!')
        break
    else:
        print(solucion)
        intento += 1

if intento == INTENTOS_TOTALES:
    print('Ooohhh, has perdido. Inténtalo de nuevo!!')
