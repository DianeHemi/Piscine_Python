def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Returns:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("Expected a function")

    res = []
    try:
        for element in iterable:
            if function_to_apply(element) is True:
                yield element
    except Exception as e:
        raise AssertionError(str(e)) from None
