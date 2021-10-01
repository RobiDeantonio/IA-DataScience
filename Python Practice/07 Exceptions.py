
def palindrome(string):
    try:
        if len(string)==0:
            raise ValueError('can not give a empty chain')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def run():

    word = input('Enter a word: ')
    try:
        print(palindrome(word))
    except TypeError:
        print('Only can get into strings')


if __name__=='__main__':
    run()
