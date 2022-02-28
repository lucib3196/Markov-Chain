import numpy as np
import sympy as sym

class Markov: 
    def __init__(self, system_size):
        self.ss = system_size

    def set_transition(self, transition_probability):
        if len(transition_probability) != (self.ss *self.ss):
            return  ValueError("List too short." )
        self.set_transition = transition_probability

Markov(3)
Markov.set_transition([])


