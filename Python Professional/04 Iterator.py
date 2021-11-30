my_list = [1,2,3,4,5]
my_iter = iter(my_list)


while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break


