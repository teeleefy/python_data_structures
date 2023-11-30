def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if isinstance(collection, dict):
        if sought in collection.values():
            # print(f"{sought} is present in this collection.")
            return True
        else:
            return False
    elif isinstance(collection, set):
        if sought in collection:
            return True
        else:
            return False
    else: 
        # isinstance(collection, list) or isinstance(collection, str) or isinstance(collection, tuple):
        # return print(f"This is NOT a dict or set")
        if start == None:
            for item in collection:
                if item == sought:
                    return True
                else:
                    return False
        else:
            while start < len(collection):
                if collection[start] == sought:
                    return True
                else:
                    start +=1
            return False
        

    