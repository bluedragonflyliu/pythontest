from random import randrange
num = input("how many dice?")
sides = input("how many sides per die?")
sum = 0
for i in range(num):
    sum +=randrange(sides)+1
print "the result is",sum
