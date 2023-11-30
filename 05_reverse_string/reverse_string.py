def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # THIS DIDN'T WORK. REPLACE REPLACES EVERY INSTANCE OF THAT LETTER WITH THE NEW LETTER
    # length = len(phrase)-1
    # index= 0
    # new_phrase = phrase
    # for letter in phrase:
    #     print(index)
    #     print(length)
    #     new_phrase = new_phrase.replace(((new_phrase)[index]),((phrase)[length]))
    #     index= index + 1
    #     length= length -1
    #     print(index)
    #     print(length)
    #     print(new_phrase)
        
    phrase = phrase[::-1]
    print(phrase)
# reverse_string('taco')

reverse_string('cottoncandy')
# print(('taco')[1])

# print(('rubiks').replace('r','c'))
