
def divisors(num):
    try:
        if num < 0:
            raise ValueError('You must enter a positive number')
        divisors = [divisor for divisor in range(1,num+1) if num % divisor == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input('Enter a number: '))
        print(divisors(num))
        print('End the program')
    except ValueError:
        print('You must enter a number')

if __name__=='__main__':
    run()
