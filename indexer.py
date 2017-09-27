import json
from subprocess import call
magicbucket = json.load(open('magicbucket.json'))

##Only keep video files
#print(json.dumps(magicbucket, indent=4))

#for item in magicbucket["files"]:
#    print (item["fileName"])

#///////hardcoded test values
videolist = ["Contact.mp4", "Dai Vernon CBS Interview 1987.mp4", "Joshua Jay - Talk About Tricks Vol 1.mp4", "Lee Asher - Cooking with Lee Asher Well Done.avi", "The School of Cool by Greg Wilson.mov"]
for i in videolist:
    #print(i)
    call(["vcs", i, "-U0 -n 20 -c 5 -H 200 -a 300/200 -o", i + ".jpg"])
