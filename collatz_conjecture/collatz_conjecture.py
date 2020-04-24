#!/usr/bin/env python3
'''
Author: Matuesz Maly
CollatzConjecture algorithm implemented in Python
'''
class CollatzConjecture():
    def __init__(self, n):
        self.n = n
        counter = 0
        sequence = []
   
        n, counter, sequence = self.compute(self.n,counter,sequence)
        
        self.print_result(n, counter, sequence)

    def compute(self, n, counter, sequence):

        if n == 1:
            counter += 1
            sequence.append(n)
            return n, counter, sequence
        elif n % 2 ==0:
            counter += 1
            sequence.append(n)
            return self.compute((n // 2), counter, sequence)
        else:
            counter += 1
            sequence.append(n)
            return self.compute((n * 3 + 1), counter, sequence)

    def print_result(self, n, counter, sequence):
        self.n = n
        self.counter = counter
        self.sequence = sequence

        print(f"Reached {self.n} after {self.counter} loops!")
        print("Sequence: ", *self.sequence)

collatzConjecture(int(input("Enter a number: ")))

