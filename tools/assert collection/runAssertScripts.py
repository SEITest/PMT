import os
import sys
import subprocess


subjectName = []
# subjectName = ['assertj-core-assertj-core-1.7.1', 'mina-core', 'pmd-src-5.2.1/pmd-core', 'commons-math']
# , 'jfreechart-1.0.19'
############################################################################################


# path = '../runnableSubjects'

# largerSubjects
subjectListFilePath = 'final_project.txt'
classAssertScriptFileName = 'classAssert.py'
testMethodScriptFileName = 'testMethodAssert.py'


def read_subjectName(path):
	cur_file = open(path)
	while True:
		line = cur_file.readline()
		if not line:
			break
		else:
			if (line[-1] == '\r') or (line[-1] == '\n'):
				subjectName.append(line[:-1])
			else:
				subjectName.append(line)
	cur_file.close()

path = '../github_subjects1'
read_subjectName("pitest_115_subject1_success.txt")

scriptsPath = os.getcwd()

for curSubName in subjectName:
	curPath = sys.path[0]

	subjectPath = path + '/' + curSubName
	classAssertPath = subjectPath + '/src'
	testMethodAssertPath = classAssertPath + '/test'

	print '\ncalculating with ' + curSubName + '...'

	os.system('cp ' + classAssertScriptFileName + ' ' + classAssertPath + '/' + classAssertScriptFileName)
	os.system('cp ' + testMethodScriptFileName + ' ' + testMethodAssertPath + '/' + testMethodScriptFileName)

	print 'python ' + classAssertPath + '/' + classAssertScriptFileName
	os.chdir(classAssertPath)
	os.system('python ' + classAssertScriptFileName)
	os.chdir(scriptsPath)

	print 'python ' + testMethodAssertPath + '/' + testMethodScriptFileName
	os.chdir(testMethodAssertPath)
	os.system('python ' + testMethodScriptFileName)
	os.chdir(scriptsPath)

print 'finished!'