print "Mary had a little lamb." # starts the rhyme
print "It's fleece was white as %s." % 'snow' # uses the formaters to continue the rhyme
print "And everywhere that Mary went." # self
print "." * 10 # just makes the periods 

end1 = "C"	# prints c
end2 = "h"	# prints h
end3 = "e"	# prints e
end4 = "e"	# prints e
end5 = "s"	# prints s
end6 = "e"	# prints e
end7 = "B"	# prints B
end8 = "u"	# prints u
end9 = "r"	# prints r
end10 = "g"	# prints g
end11 = "e"	# prints e
end12 = "r"	# prints r

# watch that comma at the end. Try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6, #concats the letters
print end7 + end8 + end9 + end10 + end11 + end12	#comma makes the words apear side by side instead of printing a new line


# Couldn't you just not use the comma , and turn the last two lines into one single-line print?
# Yes, you could very easily, but then it'd be longer than 80 characters, which in Python is bad style.