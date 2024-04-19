import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    preguntas = opciones.get(dificultad)
    
    # usar opciones desde ambiente global
    # global
    # escoger una pregunta
    n_elegido = random.choice(opciones.get(dificultad))

    # eliminarla del ambiente global para no escogerla de nuevo
    opciones.get(dificultad).remove(n_elegido)
    
    # escoger enunciado y alternativas mezcladas
    pregunta = p.pool_preguntas.get(dificultad).get("pregunta_" + str(n_elegido))
    alternativas = shuffle_alt(pregunta)
 
    return pregunta.get('enunciado'), alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')