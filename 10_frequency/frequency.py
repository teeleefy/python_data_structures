def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    count = 0
    for num in lst:
        if num == search_term: 
            count += 1
    print(count)
    return count

frequency([1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 7, 2, 3, 2, 2], 4)