def run():
    
    #squares = []
    #squares_div3 = [] 
    #for i in range(101):
    #    value = i**2
    #    if i%3 != 0:
    #        squares_div3.append(value)
    #    squares.append(value) 
    #print(squares)
    #print(squares_div3)

    ## exponent of numbers divisible by 3 with List comprenhensions
    squares = [i**2 for i in range(1,101) if i % 3 != 0]

    squares = [i for i in range(1,200) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(squares)


if __name__=='__main__':
    run()

