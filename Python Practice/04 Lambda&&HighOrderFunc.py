from functools import reduce

def run():
    
    ## lambda
    palindrome = lambda string : string == string[::-1]
    print(palindrome('ana'))

    ## Use with filter
    my_list = [1,2,3,4,5,6,7,8,9]
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    print(odd)

    ## Use with map
    squares = list(map(lambda x: x**2, my_list))
    print(squares)

    ##Use with Reduce
    all_multiplicate = reduce(lambda a,b: a*b, my_list)
    print(all_multiplicate)

if __name__=='__main__':
    run()