file= open('mbox.txt')
count = 0
for line in file:
    count=count+1
print count

fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp)

print inp[:20]

fhand= open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print line

fhand= open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za')==-1:
        continue
    print line

fname = raw_input('Enter the file name:')
try:
    fhand=open(fname)
except:
    print 'Cannot find the file name:', fname
    exit()

count=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('Subject:'):
        count = count +1
print 'There were',count,'subject lines in', fname





