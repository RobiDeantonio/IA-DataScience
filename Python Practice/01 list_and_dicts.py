def run():
    
    my_list = [1, 'hello', True, 4.5]
    my_dicts = {'firstname':'Robin', 'lastname':'Deantonio'}

    super_list = [
        {'firstname':'Robin', 'lastname':'Deantonio'},
        {'firstname':'Diego', 'lastname':'sanchez'},
        {'firstname':'Pedro', 'lastname':'perex'},
        {'firstname':'Juan', 'lastname':'Rios'}
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5,6],
        'integer_nums': [-4,-5,0,2,7],
        'floating_nums': [-0.1,2.0,3.4,8.4]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    super_dict['floating_num']

    for dict in super_list:
        print(dict)
        
if __name__ == '__main__':
    run()
