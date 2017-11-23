import csv

#puts each word of the title into a list and returns it
def getTitleWords(title):
    titleWords = [] #list that contains words (NOT CHARACTERS) from the title
    word = ""
    for ii in range(0, len(title)):
        character = str(title[ii])
        if character != ' ':  # if there's no space
            word = word + character
        else:
            if word != "":
                titleWords.append(str(word))
                word = "" #reset word for the next word
    return titleWords

#puts each word of the lyrics into a list and returns it
def getLyricWords(lyrics):
    lyricWords = []
    word = ""
    for ii in range(0, len(lyrics)):
        character = str(lyrics[ii])
        if character != ' ':  # if there's no space
            word = word + character
        else:
            if word != "":
                lyricWords.append(str(word))
                word = ""  # reset word for the next word
    return lyricWords

csvFile = "train.csv"
file = open(csvFile, "r")
csvRead = csv.reader(file, delimiter=",")
titlesList = []
lyricsList = []
wordsInTitleCount = 0
titleCount = 0

for row in csvRead:
    titlesList.append(row[0])
    lyricsList.append(row[1])
    titleCount += 1

#Read in ONE title at a time
for ii in range(0, len(titlesList)):
    wordsAreInLyrics = False
    title = str(titlesList[ii])
    titleWords = getTitleWords(title)
    lyrics = str(lyricsList[ii])
    lyricWords = getLyricWords(lyrics)

    if wordsAreInLyrics == False:
        #iterate through titleWords and try to find each titleWord in the lyricWords list
        matchCount = 0 #matchCount must equal len(titleWords) in order for wordsAreInLyrics to be true
        for jj in range(0, len(titleWords)):
            titleWord = str(titleWords[jj])
            matchFound = False
            kk = 0
            while matchFound == False and kk < len(lyricWords):
                lyricWord = str(lyricWords[kk])

                if lyricWord == titleWord:
                    matchCount += 1
                    matchFound = True
                kk += 1

        if matchCount == len(titleWords):
            if wordsAreInLyrics == False:
                wordsAreInLyrics = True
                wordsInTitleCount += 1

print(wordsInTitleCount)
print("# of songs in total: %i" % titleCount)
percentage = wordsInTitleCount / (titleCount * 1.0)
print("Percent of songs that have lyrics containing every word in the song's title: ")
print("%0.2f" % percentage)