def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        return print('Numbers are equal')
    elif a > b:
        return print('First is greater')
    else:
        return print('Second is greater')
number_compare(0,8)
    