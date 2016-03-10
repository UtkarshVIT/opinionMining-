import os
from os.path import isfile, join
import json
import re

unicodeToAsciiMap = {u'\u2019':"'", u'\u2018':"`", u'\u0022':'"', u'\u00a3':" " }
mypath = str(os.path.dirname(os.path.abspath(__file__)))

class fileIndex:
	def __init__(self, key, value):
		self.key = key
		self.value = value

def unicodeToAscii(inStr):
	try:
		return str(inStr)
	except:
		pass
	outStr = ""
	for i in inStr:
		try:
			outStr = outStr + str(i)
		except:
			if unicodeToAsciiMap.has_key(i):
				outStr = outStr + unicodeToAsciiMap[i]
			else:
				outStr = outStr + "_"
	return outStr

def checkName(fileName):
	if(re.match(r"raw+",fileName)):
		return True
	else:
		return False



count = 1
for f in os.listdir(mypath):
    if checkName(f) and f != 'rawArticle-china.txt':
    	print f
        fileToRead = open(f, 'r')
        f2 = open(f, 'w')	
        #jsonArray = json.loads(unicodeToAscii( fileToRead.read() ))
        temp = fileToRead.read()
        temp = '[' + temp + ']'
        f2.write(temp)
        f2.close()

        """
        for obj in jsonArray:
        	fileName =  obj['country'] + '_' + obj['date'] + '_' + str(count)
        	createFile =  open(fileName, 'w')
        	createFile.write( obj['content'].encode('utf-8') )
        	createFile.close()
        	count += 1
        """

"""
mypath = str(os.path.dirname(os.path.abspath(__file__)))

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print onlyfiles
"""