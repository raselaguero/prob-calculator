# todo: sombrero: un objeto sombrero que contiene bolas que debe copiarse dentro de la función.
# No inicialice la semilla aleatoria dentro de prob_calculator.py.

from random import randint
import copy


cant = 0
balls_in = {}

class Hat:

    def __init__(self, **kwargs):  # todo: ok
        global balls_in
        balls_in = copy.copy(kwargs)
        self.contents = [ k for k, v in kwargs.items() for i in range(v)]

    def draw(self, num):  # todo: ok
        out = []
        if num > len(self.contents):
            return self.contents
        else:
            for i in range(0, num):
                rdm = randint(0, len(self.contents)-1)
                out.append(self.contents.pop(rdm))
        return out



def experiment(hat, wait_balls, num_balls_drawn, num_experiments):
    global cant
    if num_experiments > 0:
        cont = acerted = 0
        out = hat.draw(num_balls_drawn)
        for k, v in wait_balls.items():
            for i in range(len(out)):
                if out[i] == k:
                    cont += 1
                    if cont == v:
                        acerted += 1
                        if acerted == len(wait_balls):
                            cant += 1
                            break
            cont = 0
        hat = Hat (**balls_in)
        experiment(hat, wait_balls, num_balls_drawn, num_experiments-1)
        prob = cant / num_experiments
        return prob
