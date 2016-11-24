def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new
r = repeater(12)
#print r.next()
r.next()
print r.send("hello, world!")
