# Exercises for chapter 2:

# Name: Tharathorn (Joy) Rimchala
# Problem 2.1
print 'Problem 2.1'
print '-------------------'
print 'Answer is commented in chapter2_exercise.py'
# zipcode = 02132 command attempts to assign 02132 as an integer to variable ZIPCODE, but int cannot start with 0.
# zipcode number should be assigned as string (zipcode = "02132") rather than as int. 
print ''

# Problem 2.2
print 'Problem 2.2'
print '-------------------'
print 5
# Assign value to x
x = 5
print 'x = 5'
print 'x + 1 = ' + str(x+1)
print ''

# Problem 2.3
print 'Problem 2.3'
print '-------------------'
# Assign values to variables
width = 17
height = 12.0
delimiter = '.'

a1 = width/2
print '1. width/2 = ' + str(a1) + ' (' + str(type(a1)) + ')'
a2 = width/2.0
print '2. width/2.0 = ' + str(a2) + ' (' + str(type(a2)) + ')'
a3 = height/3
print '3. height/3 = ' + str(a3) +  ' (' + str(type(a3)) + ')'
a4 = 1 + 2 * 5
print '4. 1 + 2 * 5 = ' + str(a4) + ' (' + str(type(a4)) + ')'
a5 = delimiter * 5
print '5. delimiter * 5 = ' + str(a5) + ' (' + str(type(a5)) + ')'
print ''

# Problem 2.4
print 'Problem 2.4'
print '-------------------'

from math import pi 
# Assign variables 2.4.1
r = 5.0
# Compute answers 2.4.1
v = (4.0/3.0)*pi*r**(3)
# Output 2.4.1
print '1. Volume of a sphere with radius 5 is : ' + str(v)
# Assign variables 2.4.2
price = 24.95
discounted = 0.6
ship1 = 3.0
shipN = 0.75
Ncopy = 60.0
# Compute answer 2.4.2
bookcost = discounted*price*Ncopy
shipcost = ship1 + shipN*(Ncopy-1)
wholecost = bookcost + shipcost
# Output 2.4.2
print '2. Total wholesale cost for 60 copies is : ' + str(wholecost)

# Assign variables 2.4.3
ti_hr = 6
ti_min = 52
ti_sec = 0 

# Compute answer 2.4.3
from math import floor
dt_easy = (8*60 + 15)*2.0 				#sec
dt_tempo = (7*60 + 12)*3.0 				#sec
dt_tot = dt_easy + dt_tempo				#sec
tis = ti_hr*3600 + ti_min*60 + ti_sec	#sec
tfs = tis + dt_tot						#sec
tend_hr = int(floor(tfs/3600))			#hr
tend_min = int(floor((tfs%3600)/60))	#min
tend_sec = int(tfs%60)					#sec

# Output 2.4.3
print ('3(1) Time spent running : ' + 
	str(int(floor(dt_tot/3600))) + ' hours, ' + 
	str(int(floor(dt_tot%3600)/60)) + ' mins, ' + 
	str(int(floor(dt_tot%60))) + ' secs')
print ('3(2) Time I get home : ' + 
	str(tend_hr) + ':' + 
	str(tend_min) + ':' + 
	str(tend_sec) )