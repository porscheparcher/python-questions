def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if b == a:
        print('Numbers are equal')
    elif a > b:
        print('First is greater')
    elif b > a:
        print('Second is greater')

print(number_compare(1, 1))
print(number_compare(-1, 1))
print(number_compare(1, -2))
    