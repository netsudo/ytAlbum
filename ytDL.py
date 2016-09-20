import pafy
import os
import sys
import subprocess
import re
from collections import namedtuple

class downloadProcess:
    def __init__(self):
        self.artistName = ''
        self.albumName = ''
        self.downloadLink = ''

    def downloadMp3(self):
        video = pafy.new(self.downloadLink)
        bestaudio = video.getbestaudio(preftype='m4a')

        bestaudio.download()

    def grabDescrip(self):
        video = pafy.new(self.downloadLink)
        vidDescription = video.description

        while True:
            try:
                if vidDescription != None:
                    return vidDescription.encode('utf-8').splitlines()
                else:
                    break

            except:
                continue

def uselessLines():
    good_list = []
    for line in downloadiT.grabDescrip():
        if re.search(r'^.*\d+:\d\d', line):
            good_list.append(line)

    return good_list

def numberedCheck():
    good_list = []
    line = uselessLines()[0]
    if line.startswith('1.') and not line[0].startswith('1. '):
        return 0
    elif line.startswith('1. '):
        return 1
    elif line.startswith('(1)') and not line.startswith('(1) '):
        return 2
    elif line.startswith('(1) '):
        return 3
    elif line.startswith('1-') and not line.startswith('1- '):
        return 4
    elif line.startswith('1 - '):
        return 5
    elif line.startswith('1 -') and not line.startswith('1 - '):
        return 6
    elif line.startswith('1- '):
        return 7
    elif line.startswith('01.') and not line.startswith('01. '):
        return 8
    elif line.startswith('01. '):
        return 9
    elif line.startswith('01 - '):
        return 10
    elif line.startswith('01- '):
        return 11
    elif line.startswith('01-') and not line.startswith('01- '):
        return 12
    elif line.startswith('01 -') and not line.startswith('01 - '):
        return 13
    else:
        return False

def numberReplace():
    i = 0
    unnumberedList = []
    bulletType = numberedCheck()
    if bulletType == 0:
        for line in uselessLines():
            unnumberedLine = line.replace(str(i + 1) + '.', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 1:
        for line in uselessLines():
            unnumberedLine = line.replace(str(i + 1) + '. ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 2:
        for line in uselessLines():
            unnumberedLine = line.replace('(' + str(i + 1) + ')', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 3:
        for line in uselessLines():
            unnumberedLine = line.replace('(' + str(i + 1) + ') ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 4:
        for line in uselessLines():
            unnumberedLine = line.replace(str(i + 1) + '-', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 5:
        for line in uselessLines():
            unnumberedLine = line.replace(str(i + 1) + ' - ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 6:
        for line in uselessLines():
            unnumberedLine = line.replace(str(i + 1) + ' -', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 7:
        for line in uselessLines():
            unnumberedLine = line.replace(str(i + 1) + '- ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 8:
        for line in uselessLines():
            if i < 10:
                unnumberedLine = line.replace('0' + str(i + 1) + '.', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + '.')

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 9:
        for line in uselessLines():
            if i < 10:
                unnumberedLine = line.replace('0' + str(i + 1) + '. ', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + '. ')

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 10:
        for line in uselessLines():
            if i < 10:
                unnumberedLine = line.replace('0' + str(i + 1) + ' - ', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + ' - ')

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 11:
        for line in uselessLines():
            if i < 10:
                unnumberedLine = line.replace('0' + str(i + 1) + '- ', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + '- ')

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 12:
        for line in uselessLines():
            if i < 10:
                unnumberedLine = line.replace('0' + str(i + 1) + '-', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + '-')

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 13:
        for line in uselessLines():
            if i < 10:
                unnumberedLine = line.replace('0' + str(i + 1) + ' -', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + ' -')

                unnumberedList.append(unnumberedLine)

        return unnumberedList

def timeStampSplit():
    songList = numberReplace()
    times = []
    names = []
    songInfo = namedtuple('songInfo', ['name', 'time'])
    REGEXS = [re.compile(r) for r in [
            r'(?P<time>\d+:\d+)\s+(?P<name>.*)$',
            r'(?P<name>.*)\s+(?P<time>\d+:\d+)$',
    ]]

    for item in songList:
        for r in REGEXS:
            m = r.match(item)
            if m:
                si = songInfo(**m.groupdict())
                names.append(si.name)
                times.append(si.time)

                break
        else:
            print 'oh oh' + repr(item)
    return names, times

def songSplit(times, names):
    i = 0
    j = 1
    for time in times:
        subprocess.call(["ffmpeg", "-i", "Audio/" "Night Runner - Starfighter [Full Album].m4a", "-acodec", "copy",
        "-t", times[j], "-ss", times[i], names[i] + ".m4a"])
        i+=1
        j+=1


downloadiT = downloadProcess()
downloadiT.downloadLink = "https://www.youtube.com/watch?v=c5LCmQC_KeU"

if __name__ == '__main__':
    names, times = timeStampSplit()
    songSplit(times, names)
