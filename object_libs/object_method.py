import inspect


def call_method(obj, method_name, *args, **kwargs):
    # Get the method from the object
    method = getattr(obj, method_name)
    sig = inspect.signature(method)
    # Check if the method requires any additional arguments
    if not len(sig.parameters):
        # Call the method without any arguments if not
        return method()
    else:
        # Pass the arguments to the method if they are needed
        return method(*args, **kwargs)
