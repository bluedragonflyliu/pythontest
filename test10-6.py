#numberlines.py
import fileinput
for line in fileinput(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print '%-40s # %2i' % (line.num)
