def safe_cast(val, to_type, default=None):
    """
    Perform a safe typecasting of a value
    
    :param val: value to cast to the desired type
    :param to_type: function used to cast to the desired type
    :param default: if the value cannot be casted, this value is returned
    :return: the original value casted into the specific type
    """
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default
