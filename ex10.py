tabby_cat = "\tI'm tabbed in."
# \t will insert a tab
persian_cat = "I'm split\non a line"
# \n will start a new line
backlash_cat = "I'm \\ a \\ cat."
# \\ will add a forward slash

fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* \t\a\vASCII Catnip\n\t* Grass
'''
# """ will start a multiline string """ ends it

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i
# don't use this unless you want to b e annoyed