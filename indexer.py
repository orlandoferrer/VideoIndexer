import json
from subprocess import call
magicbucket = json.load(open('magicbucket.json'))

##Only keep video files
#print(json.dumps(magicbucket, indent=4))

#with open('download.txt', 'a') as file:
#	for item in magicbucket["files"]:
#		file.write(item["fileName"])
    	#print (item["fileName"])

#///////hardcoded test values
#videolist = ["Contact.mp4", "Dai Vernon CBS Interview 1987.mp4", "Joshua Jay - Talk About Tricks Vol 1.mp4", "Lee Asher - Cooking with Lee Asher Well Done.avi", "The School of Cool by Greg Wilson.mov"]
#videolist = ["A New World-PBDD5Wv6O9U.webm", "Stars Of Magic 1 (Paul Harris).mp4", "DMC meets MICHAEL VINCENT-RmeQgKQrYts.mkv", "triad-coins-71306.mov", "'RAW' Footage of Chris Kenner- Out Of Control-DM6zuzlaUVA.mkv", "ONE DAY with Bryan Miles  Episode 3 - HD 720p [File2HD.com].mp4"]
#for i in videolist:
#    print(i)
#    call(['vcs "' + i + '" -U0 -n 20 -c 5 -H 200 -a 300/200 -o "' + i + '".jpg'])

#filenamequotes = '"A New World-PBDD5Wv6O9U.webm"'
#params = "-U0 -n 20 -c 5 -H 200 -a 300/200 -o"

##wip test
#call(["vcs", filenamequotes, params, filenamequotes + ".jpg"])
#call('vcs "A New World-PBDD5Wv6O9U.webm" -U0 -n 20 -c 5 -H 200 -a 300/200 -o "A New World-PBDD5Wv6O9U.webm.jpg"')


##working
#call(["vcs", "A New World-PBDD5Wv6O9U.webm", "-U0", "-n 20", "-c 5", "-H 200", "--autoaspect", "-o", "A new world.jpg"])

#working
#for i in videolist:
#	call(["vcs", i, "-U0", "-n 20", "-c 5", "-H 200", "--autoaspect", "-o", i + ".jpg"])