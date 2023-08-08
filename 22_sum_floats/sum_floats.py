def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    float_list = []
    result = 0
    for el in nums:
        if isinstance(el, (float)):
            float_list.append(el)
        else:
            continue
    for i in range(0,len(float_list)):
        result = result + float_list[i]
    return result
print(sum_floats([1.5, 2.4, 'awesome', [], 1]))
print(sum_floats([1, 2, 3]))
