def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    
    if len(lst) >= 1:
        last = lst[len(lst)-1]
        return print(last)
    else:
        return print(None)

last_element([1,2,3,'bob'])