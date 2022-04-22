from unittest import result
import numpy as np
import QueueModule
import enum

class Animal(enum):
    CAT = 1,
    DOG = 2

def appear(animal : Animal):
    if type == Animal.CAT:
        return np.random.poisson(1.5)
    else:
        return np.random.poisson(3)

def wait(animal : Animal):
    if type == Animal.CAT:
        return np.random.exponential(5)
    else:
        return np.random.exponential(3)

def goToWork(working_hours, queue_size):
    pass
    


def simulate(days, working_hours, queue_size):
    results = []

    for d in range(days):
        results += goToWork(working_hours, queue_size)

    return results        
        
def main():
    days = 1 # Should be 100
    working_hours = 12 # out of 24
    queue_size = 10
    
    results = simulate(days, working_hours, queue_size)

    # results analysis

if __name__ == "__main__":
    main()
