# Exercises for chapter 3:
# Name: Tharathorn (Joy) Rimchala
# Problem 3.1
print 'Problem 3.1'
print '-------------------'

# repeat_lyrics()

# def print_lyrics():
# 		print "I'm a lumberjack, and I'm okay."
# 		print "I sleep all night and I work all day."

# def repeat_lyrics():
# 	print_lyrics()
# 	print_lyrics()


print 'Calling function before definition results in the following error message:'
print """ NameError: name \'repeat_lyrics\' is not defined """
print 'This error arises because \'repeat_lyrics\' was called before its define declaration.'
print ''

# Problem 3.2
print 'Problem 3.2'
print '-------------------'

# def repeat_lyrics():
# 	print_lyrics()
# 	print_lyrics()

# def print_lyrics():
# 		print "I'm a lumberjack, and I'm okay."
# 		print "I sleep all night and I work all day."

# repeat_lyrics()

print """Calling \'print_lyrics\' is within \'repeat_lyrics\' in the main script does not cause any error. 
At this point in the main script, both functions are already defined. As such, the script compiles and runs without errors."""
print ''

# Problem 3.3
print 'Problem 3.3'
print '-------------------'
def right_justify(instr):
	endpos = 70
	strpos = endpos - len(instr) + 1
	outpos = ' '*strpos + instr

	print outpos

s = 'RampUp'
print 'right_justify(' + s + ') returns :'
right_justify(s)

print ''

# Problem 3.4
print 'Problem 3.4'
print '-------------------'
print '3.4.1'
def print_spam():
	print 'spam'

def do_twice(f):
	f()
	f()

do_twice(print_spam)
print ''

print '3.4.2'
def print_spam_v2(instr):
	print 'spam'

def do_twice_v2(f, instr):
	f(instr)
	f(instr)

instr = 'spam'
do_twice_v2(print_spam_v2, instr)
print ''

print '3.4.3-4'
def print_twice(instr):
	print instr
	print instr

do_twice_v2(print_twice, instr)
print ''

print '3.4.5'
def do_four(f, instr):
	do_twice_v2(f, instr)
	do_twice_v2(f, instr)

do_four(print_twice, instr)
print ''