
print 'Hello'

n = 5
while n >0:
     print n
     n = n-1
print'Blastoff!'



friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print 'Happy New Year:', friend
print 'Done!'

count = 0
for number in [1,2,3,4,5,6,7,8]:
    count = count+1
print 'Count:', count

total = 0
for intervar in [1,1,1,1,1,1]:
    total = total + intervar
print 'Total:',total

t = [1,2,3,4,5,6]
x = len(t)
y = sum(t)
z = max (t)
a = min (t)
print x, y, z, a

t = ['as','dw']
x = len(t)
# y = sum(t) for int
print x

def mine (values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

o = [1,2,3,4,5,6]
b= mine(o)
print b

while True:
    line = raw_input('>')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print line
print('Done!')

