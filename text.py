while True:
    input = raw_input('>')
    if input == 'done':
        break
    try:
        total=total+int(input)
        count=count+1
    except:
        print 'Error'
        continue

avg = float(total)/count
print total, count, avg


