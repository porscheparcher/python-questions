def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)
    digit_count1 = {}
    for digit in num1_str:
        digit_count1[digit] = digit_count1.get(digit, 0) + 1
    
    digit_count2 = {}
    for digit in num2_str:
        digit_count2[digit] = digit_count2.get(digit, 0) + 1

    if digit_count1 == digit_count2:
        return True
    else:
        return False

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
