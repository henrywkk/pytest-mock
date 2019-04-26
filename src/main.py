from config import my_config

def my_func():
    enabled_list = []
    for key in my_config:
        item = my_config[key]
        if item['Enabled'] == 'True':
            print('{0} is enabled'.format(key))
            enabled_list.append(key)
        else:
            print('{0} is NOT enabled'.format(key))
    return enabled_list

if __name__ == '__main__':
    _ = my_func()