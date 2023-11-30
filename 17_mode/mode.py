def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    #Tried a few things that didn't work...
    #Had to refer to solution...
    # firstnum = num[0]
    # count = 0
    # count2= 0
    # nums = num.sort()
    # for num in nums:
     

     # Make frequency counter of num:freq
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        print(counts)
    # find the highest value (the most frequent number)

    max_value = max(counts.values())

    # now we need to see at which index the highest value is at

    for (num, freq) in counts.items():
        if freq == max_value:
            return num



mode([2, 2, 3, 3, 2])

