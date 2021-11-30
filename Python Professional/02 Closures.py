def make_multiplier(x):

    def multiplier(n):
        return x*n
    
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

#print(times10(3))
#print(times4(3))
#print(times10(times4(2)))

########################################

def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, 'Only can to use strings'
        return string*n

    return repeater

def run():
    repetidor = make_repeater_of(3)
    print(repetidor('HoLa'))

if __name__== '__main__':
    run()

