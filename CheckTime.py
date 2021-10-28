from timeit import default_timer
from datetime import timedelta


class CheckTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        def wrapper_fn():
            start = default_timer()
            result = self.func(*args, **kwargs)
            end = default_timer()
            print(f"[{self.func.__name__}]: {timedelta(seconds=end - start)} sec\nresult : {result}")
            return result

        return wrapper_fn()
