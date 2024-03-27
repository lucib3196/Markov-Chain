# Markov Chain
A markov chain allows us to predict the outcome of an event given previous outcomes. 
## Matrix of Transition Probability
Let's consider that we had a simple bike sharing program with only 3 stations; A, B and C.

Assuming each bike needs to be returned at the end of the day, such that all bikes are at some station. 

We want to model the movement of bikes from day to day. We find that over a one day period the 
- of the bikes borrowed from station A, 30% are returned to station A, 50% end up at station B, and 20% end up at station C.
- of the bikes borrowed from station B, 10% end up at station A, 60% have been returned to station B, and 30% end up at station C
- of the bikes borrowed from station C, 10% end up at station A, 10% end up at station B, and 80% are returned to station C.

We can represent the following as a Transition Matrix of Probability. This matrix gives us the change in probability in each type of change in a given system. 

$$T = \begin{bmatrix}
    \ &A & B & C \\
    A & 0.3 & 0.5 & 0.2 \\
    B & 0.1 & 0.6 & 0.3 \\
    C & 0.1 & 0.1 & 0.8
\end{bmatrix}
$$

## Calculating Change in State
The transition matrix shows the probabilities for transitions between states at two consecutives times. We need a way to represent the distribution among these states at a particular point in time. 

To do this we can set up a **State Vector/State Matrix**($X_0$) which shows the current state. 

For example lets say the current distribution of bikes is 
A: 0.30
B: 0.50
C: 0.20
Our transition vector $X_0 = [0.30,0.5,0.2]$ 

And we are interested in finding the change after one day $X_1$

$$X_1 = \begin{bmatrix} & 0.3 &  0.5 &  0.2 \end{bmatrix} \times \begin{bmatrix}
    & 0.3 & 0.5 & 0.2 \\
    & 0.1 & 0.6 & 0.3 \\
   & 0.1 & 0.1 & 0.8
\end{bmatrix}
$$
$$X_1 = [0.16, 0.47, 0.37]$$



## Update Log 
## Ver 1.2 
Added Steady State Matrix 
## 3/7/2022
- Jupyter Notebook File Unchanged 
- Added Markov Chain Class still in the work, needs to add steady state matrix to the class.
## 3/27/2024
- Updated Markov Chain Notebook and moved somethings around 
