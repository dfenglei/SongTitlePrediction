import csv

# read through the song data csv
# extract the lyrics and take out the end lines and Punctuations from them AND lowercase them
# put the titles in the first column of the NEW csv file
# put the no end line lyrics in the second column of the NEW csv file

csvFile = "../songdata.csv"
file = open(csvFile, "r")
csvRead = csv.reader(file, delimiter=",")
titlesList = []
lyricsList = []

for row in csvRead:
    # skip the first line
    if row[3] != "text":
        titlesList.append(row[1])
        lyricsList.append(row[3])

newLyricsList = []
for ii in range(0, len(lyricsList)):
    lyrics = str(lyricsList[ii].lower())
    newLyrics = lyrics.replace('\n', " ").replace(',', " ").replace('.', " ").replace('?', " ").replace('!', " ")\
        .replace('\'', "").replace('\"', " ").replace(':', " ").replace(';', " ").replace('(', " ").replace(')', " ")\
        .replace('[', " ").replace(']', " ").replace('_', " ")
    newLyricsList.append(newLyrics)
    
newTitlesList = []
for ii in range(0, len(titlesList)):
    title = str(titlesList[ii].lower())
    newTitle = title.replace('\n', " ").replace(',', " ").replace('.', " ").replace('?', " ").replace('!', " ")\
        .replace('\'', "").replace('\"', " ").replace(':', " ").replace(';', " ").replace('(', " ").replace(')', " ")\
        .replace('[', " ").replace(']', " ").replace('_', " ")
    newTitlesList.append(newTitle)


# now add them to a new csv file
newCSV = open("songdatarevised.csv", "w")
with newCSV:
    writer = csv.writer(newCSV)
    for jj in range(0, len(newTitlesList)):
        title = str(newTitlesList[jj])
        songLyric = str(newLyricsList[jj])
        dataRow = [[title, songLyric]]
        writer.writerows(dataRow)
