def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    # count=0
    # i=1
    # for num in nums:
    #     # seen.add(num)
    #     if num < nums[i]:
    #         print(f"second {num}")
    #         print(f"third {number}")
    #         count+=1
    #         i+=1
    # print(count)
    # return count

    count = 0
    my_range = range(len(nums))
    print(my_range)
    for i in my_range:
        # print(f"i is {i}")
        range_2 = range(i + 1, len(nums))
        # print(f"This is range 2: {range_2}")
        for j in range_2:
            # print(f"j is {j}")
            if nums[j] > nums[i]:
                count += 1
                print(f"Your new count is {count}")

    return count
