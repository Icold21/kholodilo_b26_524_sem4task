import time
from copy import deepcopy
from contextlib import contextmanager

@contextmanager
def timer_ctx():
    t = time.perf_counter()
    try:
        yield
    finally:
        t = time.perf_counter() - t
        print(f"{t:.2f}")

class Timer():
    def __init__(self):
        self.time = None
        self.delta_container = None
        self.entered = False
    
    def __enter__(self):
        self.entered = True
        self.time = time.perf_counter()
        return self.delta_container
    
    def __exit__(self, exc_type, exc, tb):
        if self.entered:
            self.entered = False
            self.delta_container = deepcopy(time.perf_counter() - self.time)
            return self.delta_container
        self.time = None
            

if __name__ == '__main__':
    timer = Timer()
    with timer:
        time.sleep(1)
    print(f"{timer.delta_container:.2f}")
    
    with timer_ctx():
        time.sleep(1)