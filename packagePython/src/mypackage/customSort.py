from functools import cmp_to_key


def compare(pair1, pair2):


    number1, word1 = pair1
    number2, word2 = pair2
    if number1 == number2:
        if word1 < word2:
            return -1
        else:
            return 1
    if number1 < number2:
        return -1
    else:
        return 1

compare_key = cmp_to_key(compare)


"""
    # List of tuples
 l = [(3, 'aaa'), (1, 'bbbb'), (3, 'ab'), (2, 'aaa')]
 
 # Sort with key on first and second element of each tuple
 sorted(l, key = lambda x: (x[0], x[1]))
[(1, 'bbbb'), (2, 'aaa'), (3, 'aaa'), (3, 'ab')]
    """