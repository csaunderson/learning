import shelve
shelfFile = shelve.open('mydata')

type(shelfFile)
print(shelfFile['cats'])
shelfFile.close()
