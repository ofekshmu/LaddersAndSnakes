from logging import exception
import numpy as np
import QueueModule
from enum import Enum

WAITING_CONST = (5, 3)
WAITING_CONST_B3 = (5/3, 1)

class Animal(Enum):
    CAT = 1,
    DOG = 2,
    BUNNY = 3,
    TURTLE = 4

class Case(Enum):
    A = 1,
    B1 = 2,
    B2 = 3,
    B3 = 4

def appear(animal : Animal): # 0 - inf
    if animal == Animal.CAT:
        return np.random.poisson(1.5)
    else:
        return np.random.poisson(3)

def wait(customer : Animal, provider: Animal, case: Case):
    multiplier = 0.5 if case == Case.B2 else 1
    (lambda_cat, lambda_dog) = WAITING_CONST_B3 if provider == Animal.TURTLE else WAITING_CONST
    
    if customer == Animal.CAT:
        return np.random.exponential(multiplier*lambda_cat)
    elif customer == Animal.DOG:
        return np.random.exponential(multiplier*lambda_dog)
    else:
        raise exception(f"Value Error: {customer}")


def getPayment(animal: Animal): 
    if animal == Animal.CAT:
        return 3
    elif animal == Animal.DOG:
        return 1
    else:
        raise exception(f"Value Error: {animal}")

def goToWork(working_hours, case: Case):
    
    # ------------------- Initialize work day -------------------
    time = 1                        # Initial time stamp
    maxTime = working_hours*60      # resolution in min
    q_data = 0                           # will hold the sum standing in line each day

    client = None                   # who am i currently serving - Dog/Cat
    ttl = -1                        # time to leave - how much time is left until a client finished its treatment
    ttc = -1                        # time to cat - how much time until a cat arrives 
    ttd = -1                        # time to dog
    revenue = 0                     # will hold the daily income
    
    statistics = {Animal.DOG: 0,    # dogs accepted 
                  Animal.CAT: 0,    # cats accepted
                  'C': 0,           # dogs rejected
                  'D': 0 }          # cats rejected

    # Initialize queue size according to case
    if case == case.B1:
        queue_size = 20
    elif case == case.B3:
        queue_size = 9
    else:
        queue_size = 10 
    
    myQueue = QueueModule.QueueEx(queue_size)
    
    if case == Case.B3:
        extraQueue = QueueModule.QueueEx(1) # Queue for cats only
        ttl_turtles = -1                    # same as ttl for new queue
    # -----------------------------------------------------------
    # ---------------------- Stat Work day ----------------------
    while time < maxTime:
     
        if ttc == -1:                           # system does not know the next apperance of a cat, and will rand a new value
            ttc = appear(Animal.CAT)    
        if ttd == -1:
            ttd = appear(Animal.DOG)

        if ttc == 0:                            # a cat arrived at the store                                       
            if case == Case.B3:                 # In case B3, insertion is made to a different queue
                if extraQueue.isEmpty():
                    extraQueue.enqueue(Animal.CAT)
                else:
                    statistics['D'] += 1
            # ------- Standard case --------
            else:
                if myQueue.isEmpty():           # Insert a cat only if queue is empty
                    myQueue.enqueue(Animal.CAT) 
                else:
                    statistics['D'] += 1        # Cat was rejected
            # ------------------------------

        
        if ttd == 0:                            # a dog arrived at the store
            if not myQueue.isFull():
                myQueue.enqueue(Animal.DOG)
            else:
                revenue -= 0.1 
                statistics['C'] += 1

        if ttl == -1:                           # Bunny is currenly avaliable
            if not myQueue.isEmpty():
                client = myQueue.dequeue()
                ttl = round(wait(client, Animal.BUNNY, case))
        elif ttl == 0:                          # Treatment is finished
            revenue += getPayment(client)
            statistics[client] += 1
            client = None

        if case == Case.B3:
            if ttl_turtles == -1:
                if not extraQueue.isEmpty():
                    extraQueue.dequeue()        # No need to take the value popped since we know its a cat
                    ttl_turtles = round(wait(Animal.CAT, Animal.TURTLE, Case.B3))
            elif ttl_turtles == 0:
                revenue += getPayment(Animal.CAT)
                statistics[Animal.CAT] += 1


        q_data += myQueue.getSize()             # collecting queue data

        ttd -= 1                                # update time parameters
        ttc -= 1
        if ttl > -1: ttl -= 1                   # avoid reaching a ttl of negative value other than -1

        if case == Case.B3 and ttl_turtles >-1:  
            ttl_turtles -= 1
        time += 1
    
    queue_avg_size = q_data/(working_hours*60) 
    return statistics, revenue, queue_avg_size

def simulate(days, working_hours, case: Case):
    results = []

    for d in range(days):
        results.append(goToWork(working_hours, case))

    return results        
        
def analysis(results, days):
    statistics = {Animal.DOG: 0,  # dogs accepted 
                Animal.CAT: 0,  # cats accepted
                'C': 0,  # dogs rejected
                'D': 0,  # cats rejected
                'Revenue' : 0,
                'queue size': 0
                 }

    for t in results:
        for k, v in t[0].items():
            statistics[k] += v
        statistics['Revenue'] += t[1]
        statistics['queue size'] += t[2]

    statistics['Revenue'] = statistics['Revenue']/days
    statistics['queue size'] = statistics['queue size']/days

    print(f""" ~~~~~~~ Statistics for {days} days ~~~~~~~
    Dogs accepted: {statistics[Animal.DOG]} 
    Cats accepted: {statistics[Animal.CAT]} 
    Dogs rejected: {statistics['C']} 
    Cats rejected: {statistics['D']}     
    Avrage Revenue: {statistics['Revenue']}     
    Avrage Queue size: {statistics['queue size']}     
    """)

def main():
    # --- Parameters for the user to Change ---
    days = 100 # Should be 100
    working_hours = 12 # out of 24
    case = Case.B2
    # -----------------------------------------
    
    results = simulate(days, working_hours, case)
    analysis(results, days)


if __name__ == "__main__":
    main()
