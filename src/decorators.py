import functools
from datetime import datetime


def log(filename=None):
    """декоратор для логирования начала и концф выполнения функции, а также ее результатов или возникшие ошибки."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(
                            f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, Function: {func.__name__}, Result: {result}\n")
                else:
                    print(f"Function: {func.__name__}, Result: {result}")
                return result
            except Exception as err:
                if filename:
                    with open(filename, "a") as file:
                        file.write(
                            f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, Function: {func.__name__}, raised {type(err)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"Function: {func.__name__}, raised {type(err)}. {str(err)}")
                raise err

        return wrapper

    return decorator