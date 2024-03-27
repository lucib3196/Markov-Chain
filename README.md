# Markov Chain
A markov chain allows us to predict the outcome of an event given previous outcomes. 
## Matrix of Transition Probability
Let's consider that we had a simple bike sharing program with only 3 stations; A, B and C.

Assuming each bike needs to be returned at the end of the day, such that all bikes are at some station. 

We want to model the movement of bikes from day to day. We find that over a one day period the 
- of the bikes borrowed from station A, 30% are returned to station A, 50% end up at station B, and 20% end up at station C.
- of the bikes borrowed from station B, 10% end up at station A, 60% have been returned to station B, and 30% end up at station C
- of the bikes borrowed from station C, 10% end up at station A, 10% end up at station B, and 80% are returned to station C.
This can be shown in a diagram as 
![[Pasted image 20240326145448.png]]
We can represent the following as a [[Transition Matrix of Probability]]. This matrix gives us the change in probability in each type of change in a given system. 

$$T = \begin{bmatrix}
    \ &A & B & C \\
    A & 0.3 & 0.5 & 0.2 \\
    B & 0.1 & 0.6 & 0.3 \\
    C & 0.1 & 0.1 & 0.8
\end{bmatrix}
$$

## Update Log 
## Ver 1.2 
Added Steady State Matrix 
## 3/7/2022
- Jupyter Notebook File Unchanged 
- Added Markov Chain Class still in the work, needs to add steady state matrix to the class.
## 3/27/2024
- Updated Markov Chain Notebook and moved somethings around 
