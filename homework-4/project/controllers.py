def operation(a: int | None = None, b: int | None = None) -> int | None:
    """
    Operation with two numbers, returns the sum of them.
    
    Params:
        a: first number (integer) (optional)
        b: second number (integer) (optional)
    Returns:
        sum of a and b (integer) or None if any of a and b is None
    """

    if (a == None) or (b == None):
        return None

    return a + b