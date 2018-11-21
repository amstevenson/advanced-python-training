def cube(x):
    """
    The cube function returns x * x * x
    >>> cube(3)
    27
    >>> cube(-1)
    -1
    """
    return x*x*x


def squares(a, b):
    """
    returns all the squares in range a..b
    >>> squares(1,10)  # doctest:+ELLIPSIS +NORMALIZE_WHITESPACE
    [1, 4, ..., 100]
    """
    answer=[]
    for i in range(a,b+1):
        answer.append(i*i)
    return answer

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
