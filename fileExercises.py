# 7.2
fname = raw_input('Enter a file name:')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print 'NA NA BOO BOO TO YOU - You have been punk\'d!'
        exit()
    print 'Cannot find the file', fname
    exit()

count = 0
for line in fhand:
    line=line.rstrip()
    if line.startswith('Subject:'):
        count = count+1
print 'There were', count, 'subject lines in', fname



