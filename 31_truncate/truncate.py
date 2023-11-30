def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    # pepperoni = 9
    # n= 5
    # result = pe...
    my_str = ''
    length_of_phrase = len(phrase)
    start = 0
    add_this_many_times= n - 3
    if n >=3:
        if length_of_phrase < n:
            return phrase
        else:
            while start < add_this_many_times:
                my_str+= phrase[start]
                start+=1
            my_str+='...'
            return my_str
    else:
        print('Truncation must be at least 3 characters.')