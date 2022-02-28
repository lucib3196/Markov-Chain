from cgi import test
import numpy as np
import sympy as sym

class Markov: 
    def __init__(self, system_size):
        self.ss = system_size

    def set_transition(self, transition_probability):
        if len(transition_probability) != (self.ss * self.ss):
            raise  ValueError("List too short." )
        self.transition = transition_probability

    def get_transition_matrix(self):
        self.P_0 = (np.array(self.transition)).reshape(self.ss,self.ss)
        return self.P_0

    def set_initial_pop(self,initial_pop):
        X_n = np.array(initial_pop)
        self.d = X_n.sum()
        X_n = X_n/self.d
        self.X_n = X_n.reshape(self.ss,1)
    
    def get_initial_pop_matrix(self):
        return self.X_n

    def set_years(self,year):
        self.year = year

    # Generalize This to Form for system size
    def final_population(self):
        for i in range(self.year):
            Pop_final = np.matmul(self.P_0,self.X_n)
        Pop_final = np.around(self.X_n*self.d)
        msg1 = ( 'The Final Population after ', self.year, 'Years')
        return  msg1 + ('Population A: ' ,Pop_final[0,0])+('Population B: ' ,Pop_final[1,0])+('Population C: ' ,Pop_final[2,0])


test = Markov(3)
test.set_transition([0.70, 0.15, 0.15, 0.20, 0.80, 0.15,0.10,0.05,0.70])
print(test.get_transition_matrix())
test.set_initial_pop([15000,20000,65000])
print(test.get_initial_pop_matrix())


test.set_years(3)

print(test.final_population())