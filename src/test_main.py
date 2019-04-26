from main import my_func
from config import my_config


def override_config(monkeypatch, item_list):
    for key in my_config:
        item = my_config[key]
        if key in item_list:
            item['Enabled'] = 'True'
        else:
            item['Enabled'] = 'False'
        monkeypatch.setitem(my_config, key, item)


def test_my_func(monkeypatch):
    override_config(monkeypatch, ['ItemA', 'ItemB'])
    my_list = my_func()
    print(my_list)
    assert 'ItemA' in my_list
    assert len(my_list) == 2