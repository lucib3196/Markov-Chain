# What is A Markov Chain 
Markov Chains are used to model the change in population from one state to another

**Applications of Markov Chains include:**
- What Brand of soda to customers prefer Coke Pepsi or another brand
- The amount of airplanes at a given terminal 
- Voting Demographics 

# Steady State Matrix
As mentioned Markov Chains are used to model the change in population from one state to another. 

This change in probability can be expressed as the change from the $jth$ state to the $ith$ state. Represented by the number $p_{ij}$ where $0\le p_{ij} \le1$

- When $p_{ij}=0$ there is 0% probability of change in the system 
- When $p_{ij}=1$ there is 100% probability of change in the system 

P is called the **matrix of transition probability** because it gives the possible changes withing a population 

![image.png](attachment:466579ce-2166-43ce-a60f-929517d0b77e.png)

# Markov Chain Function 
## Function Parameters
- **Transition_Probability**: A list in the form of decimals will be used to form the matrix of transtion probability
- **Initial Population**: A list containing the current population 
- **Years**: The amount of time passed

The function can only deal with three populations nothing more nothing less

## Future Updates
The Function still has alot of work to be done. The following is just a list of things I want to add
- Steady State Matrix 
- Absorbing Markov Chains 
- Add parameters to choose how many populations
- Add parameters to prevent code from blowing up
