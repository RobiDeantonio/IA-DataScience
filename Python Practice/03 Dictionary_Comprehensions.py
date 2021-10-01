def run():
    
    squares = {}
    for i in range(101):
        squares[i] = i**3 
#    print(squares)

    ## 3er exponet of numbers with Dictionary comprenhensions that aren't divisible by 3
    squares = {i:i**3 for i in range(1,101) if i % 3 != 0}
    #print(squares)

    ##
    squares = {i:round(i**0.5,2) for i in range(1,10) if i % 3 != 0}
    print(squares)

if __name__=='__main__':
    run()

