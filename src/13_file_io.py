"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

foo = open(file = 'foo.txt', mode = 'r')
print(foo.read())
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open(file = 'bar.txt', mode = 'w')
bar.write('How could a 5-ounce bird possibly carry a 1-pound coconut?\n')
bar.write("Please! This is supposed to be a happy occasion. Let's not bicker and argue over who killed who.\n")
bar.write("Look, that rabbit's got a vicious streak a mile wide! It's a killer!")
bar.close()