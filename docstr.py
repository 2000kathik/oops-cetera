# docstrings:


def meow(n: int) ->str:

    
    # Meow in times.

    # param n: number of times to meow 
    # type n: int
    # raise TypeError: if n is not an int
    #  return: A string of n meows, one per line
    # rtype: str
    
    return "meow\n" * n


number: int = int(input("number: "))
meow: str = meow(number)
print(meow, end="")
