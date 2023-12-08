"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if number_of_primes <= 0:
        raise ValueError("You must pass a positive number to generate prime list")

    list = [2]
    i = 3
    while len(list) < number_of_primes:
        if( (i % 3 != 0 and i % 2 == 1 and i % 5 != 0 and i % 7 != 0) or i==3 or i ==5 or i ==7):
            list.append(i)
        
        i += 2   

    return list
