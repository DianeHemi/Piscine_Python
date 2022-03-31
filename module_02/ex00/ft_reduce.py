def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply):
        raise TypeError("Expected a function")

    it = iter(iterable)
    value = next(it)

    try:
        for element in it:
            value = function_to_apply(value, element)
    except Exception as e:
        raise AssertionError(str(e)) from None
    return value
