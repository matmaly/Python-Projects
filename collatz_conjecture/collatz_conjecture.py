#!/usr/bin/env python3
'''
Author: Matuesz Maly
CollatzConjecture algorithm implemented in Python
'''
class collatzConjecture():
    def __init__(self, n):
        self.n = n
        counter = 0
        sequence = []
   
        print(self.compute(self.n,counter,sequence))

    def compute(self, n, counter, sequence):

        if n == 1:
            counter += 1
            sequence.append(n)
            return f"Reached:  {n}\nAfter {counter} loops!\nSequence: {sequence}"
        elif n % 2 ==0:
            counter += 1
            sequence.append(n)
            return self.compute((n // 2), counter, sequence)
        else:
            counter += 1
            sequence.append(n)
            return self.compute((n * 3 + 1), counter, sequence)

collatzConjecture(int(input("Enter a number: ")))

