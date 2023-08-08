elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

elmo_list = list(elmo)
sauron_list = list(sauron)
gandalf_list = list(gandalf)

def friend_date(a, b):
    """Given two friends, do they have any hobbies in common? USE INTERSECTION idea.

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    hobbies_a = set(a[2])  # Convert the list of hobbies of friend a to a set for faster comparison
    hobbies_b = set(b[2])
    return len(hobbies_a.intersection(hobbies_b)) > 0
  

print(friend_date(elmo, sauron))
print(friend_date(sauron, gandalf))