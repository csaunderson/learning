import shelve
import pprint

cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
print(pprint.pformat(cats))
fileObj = open('/home/csaunderson/learning/myCats.py','w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()