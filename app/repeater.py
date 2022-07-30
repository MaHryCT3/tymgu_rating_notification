import time
from typing import Callable

def repeater(func: type[Callable], delay: int, *args, **kwargs) -> None:
    """Запускает функции с бесконечным потовренями с указаным делеем
    Args:
        func: function - Функцию которую нужно повторять
        delat: int - Количество секунд для повторения функции
        *args & **kwargs: Параметры для функции
    """
    while True:
        func(*args, **kwargs)
        time.sleep(delay)
