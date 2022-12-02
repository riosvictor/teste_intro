from math import sqrt

def rootSquareSolver(a, b, c):
  delta = b*b-4*a*c
  
  if delta == 0:
    r =(-b + sqrt(delta))/(2*a)
    return [r]
  else: 
    r1 = (-b + sqrt(delta))/(2*a)
    r2 = (-b - sqrt(delta))/(2*a)
    
    return [r1, r2]