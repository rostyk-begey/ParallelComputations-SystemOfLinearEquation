# Parallel Computations - System of Linear Equation

## Input data

matrix N * N  
vector N  
N = 80  
epsilon = 0.0001  

## Successive results

  T = ~0.004411s

## Multithread results

* ### 2 threads

  T: 0.006529s
  S = 0.675601
  E = 0.337801

* ### 4 threads

  T: 0.008952s
  S = 0.492739
  E = 0.123185

* ### 8 threads

  T: 0.015891s
  S = 0.277579
  E = 0.0346973

* ### 16 threads

  T: 0.022432s
  S = 0.196639
  E = 0.0122899
