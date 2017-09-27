import json
from subprocess import call
#only extract files with these extentions
videoext = ["mkv", "mp4", "mov", "avi", "wmv", "mpeg", "rmvb", "mpg", "mp5", "webm", "flv", "m4v"]


magicbucket = json.load(open('magicbucket.json'))

##Only keep video files
#print(json.dumps(magicbucket, indent=4)) #debug test

with open('download.txt', 'a') as file:
	for item in magicbucket["files"]:
		filename = item["fileName"] 
		partialname = filename[-5:]#extract last 5 characters from filename
		fileext = partialname.split(".") #file extension found at fileext[1]
		#exclude irrelevant files
		if (not fileext[0]) or \
			(".DS_Store" in filename) or \
			(".bzEmpty" in filename) or \
			(".part" in filename) or \
			(".plist" in filename) or \
			("." not in partialname):  #this condition can replace previous conditions 
			#print(filename)
			continue


		#compare fileext[1] with video extensions and only keep video files  
		if fileext[1] in videoext: 
			file.write(item["fileName"]+"\n")

