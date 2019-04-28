from config import my_config


class FuncRunner:
    
    def __init__(self):
        pass

    def the_func(self):
        print('[Line 1 of the_func()]my_config={}'.format(my_config))
        enabled_list = []
        for key in my_config:
            item = my_config[key]
            if item['Enabled'] == 'True':
                print('{0} is enabled'.format(key))
                enabled_list.append(key)
            else:
                print('{0} is NOT enabled'.format(key))
        return enabled_list
