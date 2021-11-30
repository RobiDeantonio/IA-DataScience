import time
from typing import Counter

class fibonacciIter():
    
    def __init__(self, max_iter:int):
        self.max_iter = max_iter


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        
        elif self.counter == 1:
            self.counter += 1
            return self.n2  

        else:
            self.aux = self.n1 + self.n2
            if self.counter >= self.max_iter:
                raise StopIteration
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux



    
if __name__=='__main__':

    fibo = fibonacciIter(10)

    for element in fibo:
        print(element)
        #time.sleep(0.5)

            


