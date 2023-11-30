def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    my_set = set()
    for key in d.keys():
        my_set.add(key)
    my_sorted_list = sorted(list(my_set))
    return print((my_sorted_list[0],my_sorted_list[len(d)-1]))


min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})