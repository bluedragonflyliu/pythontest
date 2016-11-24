def flatten(nested):
    try:
        try:
            nested+''
        except(TypeError):
            pass
        else :
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except(TypeError):
        yield nested


print list(flatten([1,[2,3],4,5,[6,[7,8]]]));

print list(flatten([1,[2,"sna"],4,5,[6,[7,8]]]));
