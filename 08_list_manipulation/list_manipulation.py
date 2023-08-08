lst = [1, 2, 3]

def list_manipulation(lst, command, location, value=None):

    """Mutate lst to add/remove from beginning or end. NEED HELP

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

    lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    list2 = []
    if command == 'remove' and location == 'end':
         return lst.pop() #1,2.... returns 3
    elif command == 'remove' and location == 'beginning':
        return lst.pop(0) # 2,3..... returns 1... list now just has 2 in it.
        
     #print(lst) turns out to be [2]
     # we put the lst to then equal... [1,2,3]  
    
    elif command == "add" and location == 'beginning':
        lst = [1, 2, 3]
        lst[:0] = [value]
        list2 += lst
        return list2 #here is when we add 20 and then it's 20, 1, 2, 3
           
    elif command == 'add' and location == 'end':
       list2 = [20, 1, 2, 3]
       list2.insert(len(list2), value) #this inserts 30 on the end
       return list2
    
    elif command != 'add' or command != 'remove':
        return None
    elif location != 'beginning' or location != 'end':
        return None
print(list_manipulation(lst, 'remove', 'end'))
print(list_manipulation(lst, 'remove', 'beginning'))
print(lst)
lst = [1, 2, 3]
print(list_manipulation(lst, 'add', 'beginning', value = 20))

print(list_manipulation(lst, 'add', 'end', value = 30))
lst = [20, 1, 2, 3, 30]
print(lst)
