import os

path = os.path.abspath(".")
output = open("../testMethodResult.txt", "w+")

def isclass(line):
	return "class" in line and "{" in line and ".class" not in line
	
def ismethod(line):
	return "{" in line and "public" in line or "protected" in line or "private" in line 

def analysis(file):
	input = open(file)
	currentclass = ''
	currentmethod = ''
	count = 0
	output.write(file + "\n")
	for line in input:
		if(isclass(line)):
			line = line.split(" ")
			try:
				index = line.index("class")
			except Exception, e:
				continue
			
			if currentclass != '' and currentmethod != '':
				output.write(currentclass + "," + currentmethod + "," + str(count) + '\n')
			currentclass = line[index+1]
			currentmethod = ''
			count = 0
			continue
		elif(ismethod(line)):
			end = line.rfind(")") + 1
			middle = line.find("(")
			start = line.rfind(" ", 0, middle) + 1
			if currentclass != '' and currentmethod != '':
				output.write(currentclass + "," + currentmethod + "," + str(count) + '\n')
			currentmethod = line[start:end]
			count = 0
			continue
		count += line.count("assert")
	if currentclass != '' and currentmethod != '':
				output.write(currentclass + "," + currentmethod + "," + str(count) + '\n')

for root, dirs, files in os.walk(path):
	for f in files:
		if ".java" not in f:
			continue
		newpath = root + "/"+ f
		print newpath
		analysis(newpath)
		print
		output.write("\n")
		
output.close()
