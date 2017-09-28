import json
import subprocess
#from subprocess import call
#only extract files with these extentions
backblaze = "backblaze"
bucket = "magic-bucket"
videoext = ["mkv", "mp4", "mov", "avi", "wmv", "mpeg", "rmvb", "mpg", "mp5", "webm", "flv", "m4v"]
filelist = []

magicbucket = json.load(open('magicbucket4.json'))

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

backblazesource = 'backblaze' + ':' + "\"" + bucket + "/" 
	
for i in filelist:
	print('rclone copy ' + backblazesource + i + "\"" + " videos")
	subprocess.call(["rclone", "copy" , backblazesource + i + "\"", "videos"]) 


#s = subprocess.check_output(["rclone", "copy", backblazestring, "videos"])
#print(s)

#subprocess.Popen('rclone copy ' + backblazestring + " videos", shell=True)

#testlist = ["rclone", "copy", 'backblaze:"magic-bucket/videos/youtube/10-Card Poker Deal-EPhspnS0h_U.mkv\"', "videos"]
#dirstring = "backblaze:\"magic-bucket//videos//youtube//10-Card Poker Deal-EPhspnS0h_U.mkv\""




#for i in filelist:
#	call(["vcs", i, "-U0", "-n 20", "-c 5", "-H 200", "--autoaspect", "-o", i + ".jpg"])
