import doctest


def how_long(st: str, n: int) -> str:
    """
    >>> how_long("aa", 3)
    'aa'
    >>> how_long("aa", 1)
    'AA'
    """
    return st.upper() if len(st) > n else st


doctest.testmod()