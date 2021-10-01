
def divisors(num):
        divisors = [divisor for divisor in range(1,num+1) if num % divisor == 0]
        return divisors


def run():
    num = input('Enter a number: ')
    assert num.isnumeric(),  'You must enter a number and it must be positive'
    print(divisors(int(num)))

if __name__=='__main__':
    run()
