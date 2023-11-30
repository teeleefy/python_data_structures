def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    #lst, command, location, value=None
    # append for add end
    # insert for add beginning insert(self, index, object)
    # and pop from remove end
    # pop(0) for remove beginning
    
    if command == 'add':
        if location == 'end':
            lst.append(value)
            return print(lst)
        elif location == 'beginning':
            lst.insert(0, value)
            return print(lst)
        else:
            print(None) 
            return None    
    elif command == 'remove':
        if location == 'end':
            lst.pop()
            return print(lst)
        elif location == 'beginning':
            lst.pop(0)
            return print(lst)
        else:
            print(None) 
            return None
    else: 
        print(None)
        return None


(list_manipulation([1,2,3,4,5], 'remove', 'taco')) is None
