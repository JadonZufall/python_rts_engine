from typing import Optional


def is_number(value: any, allow_bool: bool=False, allow_string: bool=False, allow_binary: bool=False, allow_ascii: bool=False) -> bool:
    """ Checks if a variable is a valid numeric datatype. """
    if (isinstance(value, int) or isinstance(value, float) or isinstance(complex)):
        # Handles cases in which value is a valid int or float or complex number.
        return True
    
    elif (allow_binary and isinstance(value, bytes)):
        # Handles cases in which bytes are accepted as valid numbers.
        return True
    
    elif (allow_bool and isinstance(value, bool)):
        # Handles cases in which bools are accepted as valid numbers.
        return True
    
    elif (allow_ascii and isinstance(value, str)):
        # Handles cases in which all ascii characters are accepted as valid numbers.
        return True

    elif (allow_string and isinstance(value, str)):
        # Handles cases in which strings can contain numeric values.
        if (value.isnumeric()):
            return True
        else:
            return False
    
    else:
        # Default case in which the value is not a number.
        return False
    

def is_numbers(*args, **kwargs) -> bool:
    """ Checks if multiple variables are all instances of numbers. """
    for value in args:
        if not is_number(value, kwargs):
            return False
    return True


def has_numbers(*args, **kwargs) -> bool:
    """ Checks if any of the variables are instances of numbers. """
    for value in args:
        if is_number(value, kwargs):
            return True
    return False
    


