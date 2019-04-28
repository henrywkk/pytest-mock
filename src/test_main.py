from main import main_run
from config import my_config


def override_config(monkeypatch, item_list):
    # Sample code on monkeypatch.setitem for dict-type config
    for key in my_config:
        item = my_config[key]
        if key in item_list:
            item['Enabled'] = 'True'
        else:
            item['Enabled'] = 'False'
        monkeypatch.setitem(my_config, key, item)


def test_my_func(monkeypatch):
    override_config(monkeypatch, ['ItemB'])
    my_list = main_run()
    print(my_list)
    assert 'ItemB' in my_list
    assert len(my_list) == 1