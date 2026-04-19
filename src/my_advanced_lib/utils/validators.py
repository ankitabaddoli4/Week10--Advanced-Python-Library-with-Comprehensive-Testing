def validate_types(**type_hints):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for name, expected in type_hints.items():
                if name in kwargs and not isinstance(kwargs[name], expected):
                    raise TypeError(f"{name} must be {expected}")
            return func(*args, **kwargs)
        return wrapper
    return decorator