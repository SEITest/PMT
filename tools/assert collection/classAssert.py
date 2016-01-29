import os

path = os.path.abspath("./test")
path2 = os.path.abspath("./main")
output = open("classResult.txt", "w+")


def isclass(line):
	if "class" not in line.split(" "):
		return False
	return ("class" in line or 'interface' in line) and "{" in line and ".class" not in line and "*" not in line and "\"" not in line
	
def ismethod(line):
	return "{" in line and "public" in line or "protected" in line or "private" in line 
	
def istargetfile(file):
	file = file.replace("Test", '')
	return file in targetfiles.keys()

def linenum(file):
	file = file.replace("Test", '')
	return targetfiles[file]

def analysis(file):
	input = open(file)
	count = 0
	for line in input:
		count += line.count("assert")
	return count
	
def classline(file):
	input = open(file)
	classcount = 0
	start = 0
	tmp = 0
	end = 0
	classname = ''
	index = 0
	for line in input:
		tmp += 1
		end += 1
		if isclass(line):
			line = line.split(" ")
			if "class" in line:
				index = line.index("class")
			elif "index" in line:
				index = line.index("interface")
			classname = line[index+1]
			classcount += 1
			start = tmp
	output.write(classname + "," + str(start) + "--" + str(end) + '\n')
	output.write("total classes = " + str(classcount) + '\n')
		
targetfiles = dict()
testfiles = dict()
paths = []
for root, dirs, files in os.walk(path2):
	for f in files:
		if ".java" not in f:
			continue
		newpath = root + "/"+ f
		paths.append(newpath)
		targetfiles[f] = 0

for root, dirs, files in os.walk(path):
	for f in files:
		if ".java" not in f:
			continue
		newpath = root + "/"+ f
		print newpath
		testfiles[f] = newpath

for file in targetfiles.keys():
	count = 0
	for path in paths:
		if file in path:
			output.write(path + "\n")
			classline(path)
			break
	for testfile in testfiles.keys():
		if file.replace(".java", '') in testfile:
			count += analysis(testfiles[testfile])
			targetfiles[file] = 1
	output.write(file.replace(".java", '') + ","+ str(count) + '\n')
			
for (key, value) in targetfiles.items():
	if value == 0:
		for path in paths:
			if key in path:
				output.write(path + "\n")
				break
output.close()
