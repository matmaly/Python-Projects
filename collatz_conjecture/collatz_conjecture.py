#!/usr/bin/env python3
'''
Author: Matuesz Maly
CollatzConjecture algorithm implemented in Python
'''
class collatzConjecture():
    def __init__(self, n):
        self.n = n
        counter = 0
   
        print(self.compute(self.n,counter))

    def compute(self, n, counter):

        if n == 1:
            counter += 1
            return f"Reached:  {n}\nAfter {counter} loops!"
        elif n % 2 ==0:
            counter += 1
            return self.compute((n // 2), counter)
        else:
            counter += 1
            return self.compute((n * 3 + 1), counter)

collatzConjecture(int(input("Enter a number: ")))

