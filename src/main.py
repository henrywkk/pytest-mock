from config import my_config
from func_runner import FuncRunner


def main_run():
    runner = FuncRunner()
    return runner.the_func()

if __name__ == '__main__':
    _ = main_run()