def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    even_list = []
    result = 1
    for number in nums:
        if number % 2 == 0:
            even_list.append(number)
        else:
            continue
    for i in range(0,len(even_list)):
        result = result * even_list[i]
    return result
        
    

print(multiply_even_numbers([2, 3, 4, 5, 6]))
print(multiply_even_numbers([3, 4, 5]))
print(multiply_even_numbers([1, 3, 5]))
           
        
       
        
