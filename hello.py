def log_function_call(func):
    def wrapper(*args, **kwargs):
       print(f"Calling function: {func.__name__}")
       result = func(*args, **kwargs)
       print(f"Function {func.__name__} executed successfully.")
       return result
    return wrapper

@log_function_call
def add_numbers(a, b):
    return a + b
result = add_numbers(2, 3)
print(result)

class DecoratorClass:
    def __init__(self, func):
       self.func = func
    def __call__(self, *args, **kwargs):
       print("Decorator class: Before function execution")
       result = self.func(*args, **kwargs)
       print("Decorator class: After function execution")
       return result

@DecoratorClass
def decorated_function():
    print("Original function")

decorated_function()
