def decorator(argument):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + argument
        return wrapper
    return real_decorator


