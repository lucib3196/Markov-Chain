from cgi import test
import numpy as np
import sympy as sym

class Markov: 
    def __init__(self, system_size):
        self.ss = system_size
    
    # Sets the transiton matrix which is the probability of a change in a system 
    def set_transition(self, transition_probability):
        if len(transition_probability) != (self.ss * self.ss):
            raise  ValueError("List too short." )
        self.transition = transition_probability
        self.P_0 = (np.array(self.transition)).reshape(self.ss,self.ss)

        # Check to see if matrix values add up to 1
        n = int((self.P_0).size ** (.5)) 
        for i in range(n):
            x= (self.P_0.transpose()[i].sum()).round(2)
            if x != 1:
                raise ValueError ('Transition Matrix Values Must add up to 1')


    # Returns Transition Matrix
    def get_transition_matrix(self):
        return self.P_0

    # Sets the initial population matrix
    def set_initial_pop(self,initial_pop):
        X_n = np.array(initial_pop)
        self.d = X_n.sum()
        X_n = X_n/self.d
        self.X_n = X_n.reshape(self.ss,1)
        # Checks if the matrix adds up to 1
        if self.X_n.sum() !=1:
            raise ValueError('Matrix Values must add up to 1')
    
    # Returns the initial population matrix
    def get_initial_pop_matrix(self):
        return self.X_n

    # Set the years 
    def set_years(self,year):
        self.year = year

    # Gets the final population after a set of years
    def final_population(self):
        # Finds the final population in the form X_n = P_0 * X_0 where n is the number of years
        
        for i in range(self.year):
            Pop_final = np.matmul(self.P_0,self.X_n)
        Pop_final = np.around(self.X_n*self.d)

        # Creates the final population 
        final_msg = ''
        for i in range(Pop_final.size):
            msg = 'Population ' + str(i) + ' : ' + str(Pop_final[i,0]) 
            final_msg += msg + '\n'
        intro_msg = ( 'The Final Population after ' + str(self.year) + ' Years')
        return intro_msg + '\n' + final_msg

    # def get_steadystate(self):
    #     for i in range((self.X_n).size):

test = Markov(3)
test.set_transition([0.75, 0.15, 0.15, 0.20, 0.80, 0.15,0.10,0.05,0.70])
print(test.get_transition_matrix())
test.set_initial_pop([15000,20000,65000])

