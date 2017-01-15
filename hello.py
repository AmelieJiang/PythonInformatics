
# first try print
print 'hello world'

# operators and operands
x= 1+1
print x
x = 100
y = 250
print x + y
x ="520"
y = "333"
print x + y


inp = raw_input('Enter Fahrenheit Temperature:')
try:
 fahr = float(inp)
 cel=(fahr-32.0)*5.0/9.0
 print cel
except:
 print 'Enter a number'

# Excercise 3.2
Hours = raw_input('Input Hours:')
Rates = raw_input('Input Rates:')
#Hours =45
#Rate = 10
try:
  Pay = 40*10+(float(Hours)-40)*1.5*float(Rates)
  print Pay
except:
  print 'You should input a number'


# Exercise 3.3
score = raw_input('Input Score:')
if score >= 0.9 and score <= 1.0 :
	print 'A'
elif score >= 0.8 and score <0.9:
	print 'B'
elif score >= 0.7 and score < 0.8:
	print 'C'
elif score >=0.6 and score < 0.7:
	print 'D'
elif score < 0.6:
	print 'F'
else :
	print 'Bad score'


and del from as elif global assert else if break except import class exec in continue finally is
def for lambda
not while or with pass yield print
raise return try