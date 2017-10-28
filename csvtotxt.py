import csv
import pdb

csvFile = "songdata.csv"
file = open(csvFile, "r")
csvRead = csv.reader(file, delimiter=",")
lyricsList = []
#Iterate through the 4th column of the csv file
for row in csvRead:
    #skip the first line
    if row[3] != "text":
        lyricsList.append(row[3])

#now take out the \n tokens in the lyrics and replace them with " "
lyricsNoEndLine = []
for ii in range(0, len(lyricsList)):
    lyrics = str(lyricsList[ii])
    #iterate through the lyric to take out the \n tokens
    newLyrics = ""
    for jj in range(0, len(lyrics)):
        character = lyrics[jj]
        if character == '\n':
            character = " "
        newLyrics = newLyrics + character
    lyricsNoEndLine.append(newLyrics)

#print each line of lyricsNoEndLine
for kk in range(0, len(lyricsNoEndLine)):
    print(lyricsNoEndLine[kk])
