import string

STRIP = string.whitespace


def to_cast(f):
    """
    Decorator to easily use a function as casting argument.

    Example:
        from decouple import config
        from decouple_plus.casting import to_cast

        @to_cast
        def to_tuple(value, delimiter=','):
            # do stuff

        ...

        # TEAMS_TREE == pepe,carl,jose;pablo,mark
        teams_tree = config('TEAMS_TREE', cast=to_tuple(';,'))
        print(teams_tree)
        >>> (('pepe', 'carl', 'jose'), ('pablo', 'mark'))

    """
    def wrapper(*args, **kwargs):
        def w(value):
            return f(value, *args, **kwargs)
        return w
    return wrapper


def _tuple_divider(value, delimiter, index):
    """
    Recursive tuple generator.

    @param value: string ('pepe, bob, jose') to divide.
    @param delimiter: collection(list, tuple, str) to divide by.
    @param index: index of divider in delimiter to divide by...
        what?!:
            delimiter[index]
    """
    values = []

    if not value:
        return

    if len(delimiter) <= index:
        return value.strip(STRIP)

    for t in value.split(delimiter[index]):
        result = _tuple_divider(t, delimiter, index + 1)

        if result:
            values.append(result)

    return tuple(values)


@to_cast
def to_tuple(value, delimiter=','):
    """
    Divides string into a tuple or tuples of tuples

    @param value: string to divide
    @param delimiter: collection to divide by (list, tuple, str)

    Example:
        >>> to_tuple('pepe, bob, jose')
        ('pepe', 'bob', 'jose')
        >>>
        >>> to_tuple(
        ...     'pepe, pepe@mail.com; bob, bob@mail.com; jose, jose@mail.com',
        ...     delimiter=';,')
        (('pepe', 'pepe@mail.com'), ('bob', 'bob@mail.com'), ...
    """
    if not (delimiter and value):
        return value

    return _tuple_divider(value, delimiter, 0)
