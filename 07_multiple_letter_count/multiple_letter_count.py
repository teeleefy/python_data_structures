def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letters_one_time = set()
    for char in phrase:
        letters_one_time.add(char)
    letter_count = dict.fromkeys(letters_one_time, 0)
    # for (alphabet, count) in letter_count.items():
    #     print(f"This letter({alphabet}) is in here this many times: {count})")
    for char in phrase:
        if char in letter_count:
            letter_count[char] += 1
    return print(letter_count)
    


multiple_letter_count('sammysosa')
