# Parallel Computations - System of Linear Equation

## Input data

matrix N * N  
vector N  
N = 80  
epsilon = 0.0001  

## Successive results

  T = ~4.5s

## Multithread results

* ### 2 threads

  T = ~5.8s  
  S = 0.77  
  E = 0.385

* ### 4 threads

  T = ~6.5s  
  S = 0.69  
  E = 0.1725

* ### 8 threads

  T = ~13s  
  S = 0.346  
  E = 0.04325

* ### 16 threads

  T = ~21.5s  
  S = 0.21  
  E = 0.013125
