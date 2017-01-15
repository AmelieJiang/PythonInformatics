# Exercise 4.1 - random

import random

for i in range(10):
    x = random.random()
    print x

y = random.randint(5,10)
print y

t = [1,2,3]
t = random.choice(t)
print t

# 4.2

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print 'I sleep all night and I work all day.'

repeat_lyrics()

# 4.6
def computePay(hour,rate):
    try:
        if hour > 40:
            pay = 40*10+(hour-40)*1.5*rate
            return pay
        elif hour<=40 and hour>=0:
            pay = hour*rate
            return pay
        else:
            print 'You should enter a positive number!'
    except:
        print 'You should enter a positive number!'

def testComputePay():
    x= computePay(45,10)
    print x
    x= computePay(10,10)
    print x
    x= computePay(50,20)
    print x
    x= computePay('dd','jj')
    print x

testComputePay()

# 4.7


def computeGrade(score):

    try:
        if score >= 0.9 and score <= 1.0:
             print 'A'
        elif score >= 0.8 and score < 0.9:
             print 'B'
        elif score >= 0.7 and score < 0.8:
            print 'C'
        elif score >= 0.6 and score < 0.7:
            print 'D'
        elif score < 0.6:
            print 'F'
        else:
            print 'Bad score'

    except:
        print 'Bad score'

x = computeGrade(0.95)
print x
x = computeGrade('perfect')
print x
x = computeGrade(10.0)
print x
x = computeGrade(0.75)
print x
x = computeGrade(0.5)
print x