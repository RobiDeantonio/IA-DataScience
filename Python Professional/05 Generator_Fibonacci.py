import time

def fibo_gen(max_it:int):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            counter += 1
            aux = n1 + n2
            n1 = n2
            n2 = aux
            yield aux
        if counter == max_it:
            break

def run():
    fibonacci = fibo_gen(5)

    for element in fibonacci:
        print(element)
        time.sleep(0.5)

if __name__=='__main__':
    run()