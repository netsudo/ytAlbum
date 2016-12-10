import pafy
import sys
import subprocess
import tempfile
import re
from collections import namedtuple

def downloadSingle(downloadLink):
    path = tempfile.mkdtemp(dir="Audio/")
    video = pafy.new(downloadLink)
    bestaudio = video.getbestaudio(preftype='m4a')
    filename = video.title + '.m4a'

    bestaudio.download(filepath=path)

    return path, filename

def downloadMp3(downloadLink):
    video = pafy.new(downloadLink)
    bestaudio = video.getbestaudio(preftype='m4a')

    bestaudio.download()

def titleGrab(downloadLink):
    video = pafy.new(downloadLink)

    return video.title + '.m4a'

def grabDescrip(downloadLink):
    video = pafy.new(downloadLink)
    vidDescription = video.description

    while True:
        try:
            if vidDescription != None:
                return vidDescription.encode('utf-8').splitlines()
            else:
                break

        except:
            continue

def uselessLines(downloadLink):
    good_list = []
    full_list = grabDescrip(downloadLink)
    for line in full_list:
        if re.search(r'^.*\d+:\d\d', line):
            good_list.append(line)

    return good_list

def numberedCheck(downloadLink):
    good_list = []
    line = uselessLines(downloadLink)[0]
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
    elif line.startswith('1:') and not line.startswith('1: '):
        return 14
    elif line.startswith('1: '):
        return 15
    elif line.startswith('01 :') and not line.startswith('1 : '):
        return 16
    elif line.startswith('1 : '):
        return 17
    elif line.startswith('01:') and not line.startswith('01: '):
        return 18
    elif line.startswith('01: '):
        return 19
    elif line.startswith('01 :') and not line.startswith('01 : '):
        return 20
    elif line.startswith('01 : '):
        return 21
    elif line.startswith(':') and not line.startswith(': '):
        return 22
    elif line.startswith(' :') and not line.startswith(' : '):
        return 23
    elif line.startswith(' : '):
        return 24
    elif line.startswith(': '):
        return 25
    elif line.startswith('-') and not line.startswith('- '):
        return 26
    elif line.startswith('- '):
        return 27
    elif line.startswith(' -') and not line.startswith(' - '):
        return 28
    elif line.startswith(' - '):
        return 29
    else:
        return False

def numberReplace(downloadLink):
    i = 0
    unnumberedList = []
    goodLines = uselessLines(downloadLink)
    bulletType = numberedCheck(downloadLink)
    if bulletType == 0:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + '.', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 1:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + '. ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 2:
        for line in goodLines:
            unnumberedLine = line.replace('(' + str(i + 1) + ')', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 3:
        for line in goodLines:
            unnumberedLine = line.replace('(' + str(i + 1) + ') ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 4:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + '-', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 5:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + ' - ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 6:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + ' -', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 7:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + '- ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 8:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + '.', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + '.', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 9:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + '. ', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i + 1) + '. ', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 10:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + ' - ', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + ' - ', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 11:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + '- ', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + '- ', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 9:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + '-', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + '-', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 13:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + ' -', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + ' -', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 14:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + ':', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 15:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + ': ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 16:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + ' :', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 17:
        for line in goodLines:
            unnumberedLine = line.replace(str(i + 1) + ' : ', '')
            i+=1

            unnumberedList.append(unnumberedLine)
        return unnumberedList

    elif bulletType == 18:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + ':', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + ':', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 19:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + ': ', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + ': ', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 20:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + ' :', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + ' :', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType == 21:
        for line in goodLines:
            if i < 9:
                unnumberedLine = line.replace('0' + str(i + 1) + ' : ', '')
                i+=1

                unnumberedList.append(unnumberedLine)
            else:
                unnumberedLine = line.replace(str(i+1) + ' : ', '')
                i+=1

                unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType==22:
        for line in goodLines:
            unnumberedLine = line.replace(':', '')

            unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType==23:
        for line in goodLines:
            unnumberedLine = line.replace(' :', '')

            unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType==24:
        for line in goodLines:
            unnumberedLine = line.replace(' : ', '')

            unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType==25:
        for line in goodLines:
            unnumberedLine = line.replace(': ', '')

            unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType==26:
        for line in goodLines:
            unnumberedLine = line.replace('-', '')

            unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType==27:
        for line in goodLines:
            unnumberedLine = line.replace('- ', '')

            unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType==28:
        for line in goodLines:
            unnumberedLine = line.replace(' -', '')

            unnumberedList.append(unnumberedLine)

        return unnumberedList

    elif bulletType==29:
        for line in goodLines:
            unnumberedLine = line.replace(' - ', '')

            unnumberedList.append(unnumberedLine)

        return unnumberedList

def descripRegex():
    REGEXS = [re.compile(r) for r in [
            r'(?P<time>\d+:\d+:\d+)\s+(?P<name>.*)$',
            r'(?P<time>\d+:\d+)\s+(?P<name>.*)$',
            r'(?P<name>.*)\s+(?P<time>\d+:\d+:\d+)$',
            r'(?P<name>.*)\s+(?P<time>\d+:\d+)$',
    ]]

    return REGEXS

def timeRegex():
    REGEXS = [re.compile(r) for r in [
            r'(?P<time>\d+:\d+:\d+)$',
            r'(?P<time>\d+:\d+)$',
    ]]

    return REGEXS

def timeStampSplit(downloadLink):
    songList = numberReplace(downloadLink)
    times = []
    names = []
    songInfo = namedtuple('songInfo', ['name', 'time'])

    for item in songList:
        for r in descripRegex():
            m = r.match(item)
            if m:
                si = songInfo(**m.groupdict())
                names.append(si.name)
                times.append(si.time)

                break
        else:
            print 'oh oh' + repr(item)
    return names, times

def pathCreator(downloadLink):
    names, times = timeStampSplit(downloadLink)
    paths = []
    temp = tempfile.mkdtemp(dir="Audio/")

    for name in names:
        path = temp + "/" + name + ".m4a"
        paths.append(path)

    return paths, times, names

def songSplit(downloadLink):
    path, times, names = pathCreator(downloadLink)
    source = titleGrab(downloadLink)
    i = 0
    j = 1
    for time in times:
        try:
            subprocess.call(["ffmpeg", "-i", source, "-acodec", "copy",
            "-to", times[j], "-ss", times[i], path[i]])
            i+=1
            j+=1
        except IndexError:
            subprocess.call(["ffmpeg", "-i", source, "-acodec", "copy",
            "-to", "5:00:00", "-ss", times[i], path[i]])
    subprocess.call(["rm", source])

    return path, names

def userPathCreator(downloadLink, timeList):
    paths = []
    temp = tempfile.mkdtemp(dir="Audio/")

    for name in timeList:
        path = temp + "/" + name + ".m4a"
        paths.append(path)

    return paths

def userSongSplit(downloadLink, timeList, titleList):
    source = titleGrab(downloadLink)
    path = userPathCreator(downloadLink, timeList)
    i = 0
    j = 1
    for time in titleList:
        try:
            subprocess.call(["ffmpeg", "-i", source, "-acodec", "copy",
            "-to", titleList[j], "-ss", titleList[i], path[i]])
            i+=1
            j+=1
        except IndexError:
            subprocess.call(["ffmpeg", "-i", source, "-acodec", "copy",
            "-to", "5:00:00", "-ss", titleList[i], path[i]])
    subprocess.call(["rm", source])

    return path
