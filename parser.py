import json
import subprocess
import os
#from subprocess import call
#only extract files with these extentions
backblaze = "backblaze"
bucket = "magic-bucket"
videoext = ["mkv", "mp4", "mov", "avi", "wmv", "mpeg", "rmvb", "mpg", "mp5", "webm", "flv", "m4v"]
filelist = []

magicbucket = json.load(open('jsonfile.json'))

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
			continue #skip if file is not relevant

		#compare fileext[1] with video extensions and only keep video files  
		if fileext[1] in videoext: 
			file.write(item["fileName"]+"\n") #keep a logfile
			filelist.append(item["fileName"])

backblazesource = 'backblaze' + ':' + "" + bucket + "/" 
	
for i in filelist:
	print('rclone copy ' + backblazesource + i + "\"" + " videos")
	subprocess.call(["rclone", "copy" , backblazesource + i, "videos"]) 

#build web page
htmlPage = open('videos2.html', 'a+')
htmlPage.write("<!doctype html> \
<html lang=\"en\"> \
<head> \
  <meta charset=\"utf-8\"> \
  <title>Video Indexer</title> \
</head> \
<body>")	


videos = os.listdir("videos")
for i in videos:
	subprocess.call(["vcs", "videos/" + i, "-U0", "-n 20", "-c 5", "-H 200", "--autoaspect", "-o", "caps/" +i + ".jpg"])
	#get time calling ffmpeg
	process = subprocess.Popen(['ffmpeg',  '-i', 'videos/' + i], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = process.communicate()
	outputstr = stdout.decode("utf-8")
	timeptr = outputstr.find("Duration: ")
	time = outputstr[timeptr:timeptr+21]
	print(time)
	htmlPage.write("File Name: " + i + "</br>" + "Duration: " + time)
	htmlPage.write("<img src=\"caps/" + i + ".jpg\">") 


htmlPage.write("</body> \
</html>")


