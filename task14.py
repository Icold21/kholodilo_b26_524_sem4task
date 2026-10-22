import time
from contextlib import contextmanager
import pathlib

@contextmanager
def log_operation(log_filename, process_name):
    exception = None
    log_ctx = ""
    
    if pathlib.Path(log_filename).exists():
        with open(log_filename, "r", encoding="utf-8") as log_datafile:
            for line in log_datafile:
                log_ctx += line
    else:
        with open(log_filename, "w", encoding="utf-8") as log_datafile:
            pass
        
    log_ctx += f"START: {process_name}\n"
    
    try:    
        yield
    except Exception as exc:
        exception = exc
    finally:
        if exception is None:
            log_ctx += f"END: {process_name}\n"
        else:
            log_ctx += f"ERROR ({exception}): {process_name}\n"
            
        with open(log_filename, "w", encoding="utf-8") as log_datafile:
            log_datafile.write(log_ctx)

if __name__ == '__main__':
    with open("data/operation.log", "w+", encoding="utf-8") as log_file:
        log_file.truncate(0)
        print(f"Logs:\n{"="*20}\n{log_file.read()}{"="*20}\n")
    
    with log_operation("data/operation.log", "Data processing"):
        time.sleep(1)
        
    with log_operation("data/operation.log", "Data processing"):
        res = 1 / 0
      
    with open("data/operation.log", "r", encoding="utf-8") as log_file:
        print(f"Logs:\n{"="*20}\n{log_file.read()}{"="*20}\n")  