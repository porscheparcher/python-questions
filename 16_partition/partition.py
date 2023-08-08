a = []
b = []
a1 = []
b2 = []
new_list = [a, b]
new_list1 = [a1, b2]
def is_even(num):
    return num % 2 == 0
    
def is_string(el):
    return isinstance(el, str)


def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    
    if fn == is_even:
        for num in lst:
            if num % 2 == 0:
                a.append(num)
            elif num % 2 != 0:
                b.append(num)
        return new_list
    elif fn == is_string:
        for el in lst:
            if isinstance(el, str):
                a1.append(el)
            else:
                b2.append(el)
        return new_list1
print(partition([1, 2, 3, 4], is_even))
print(partition(["hi", None, 6, "bye"], is_string))