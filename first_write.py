# Open the file, writable, first
baconFile = open('/home/csaunderson/learning/bacon.txt','w')
# now that it's open, write to it.
baconFile.write('Hello World!\n')
# close what you open
baconFile.close()
# read that back, Ms Smith
baconFile = open('/home/csaunderson/learning/bacon.txt','r')
print(baconFile.read())
baconFile.close()
# now that we've closed it, we can open it again to append to it
baconFile = open('/home/csaunderson/learning/bacon.txt', 'a')
#  now that we're appendable, we're going to put more content in
baconFile.write('Bacon is not a vegetable.\n')
# close what we open
baconFile.close()
# now we can repeat the readback, Ms Smith
baconFile = open('/home/csaunderson/learning/bacon.txt','r')
print(baconFile.read())
baconFile.close()