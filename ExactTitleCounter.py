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

csvFile = "../train.csv"
file = open(csvFile, "r")
csvRead = csv.reader(file, delimiter=",")
titlesList = []
lyricsList = []
exactTitleCount = 0
titleCount = 0

for row in csvRead:
    titlesList.append(row[0])
    lyricsList.append(row[1])
    titleCount += 1

#Read in ONE title at a time
word = ""
for ii in range(0, len(titlesList)):
    titleIsInLyrics = False
    title = str(titlesList[ii])
    titleWords = getTitleWords(title)
    lyrics = str(lyricsList[ii])
    lyricWords = getLyricWords(lyrics)

    #now iterate through lyricsWords to find a word that matches the FIRST word of the title (titleWords[0])
    if titleIsInLyrics == False:

        for jj in range(0, len(lyricWords)):
            lyricWord = str(lyricWords[jj])
            if titleWords != []:
                firstTitleWord = str(titleWords[0])
                # check if this word matches the FIRST title word
                if lyricWord == firstTitleWord:
                    #depending on the length of the titleWords (x number of words in the title) extract the NEXT x number of words
                    # from lyricWord and put it in a titleLyrics array/list. If titleLyrics == titleWords then increment the exactTitleCount by 1
                    wwStart = jj
                    wwEnd = wwStart + len(titleWords) #stops at after the next x number of words from the lyricWord list

                    if wwEnd <= len(lyricWords):
                        titleLyrics = []
                        titleLyrics.append(lyricWord) #takes the first matching word

                        for ww in range(wwStart+1, wwEnd):
                            lyricWord = str(lyricWords[ww])
                            titleLyrics.append(lyricWord)

                        #now check if titleLyrics == titleWords
                        #If it does then the count goes up
                        if titleLyrics == titleWords:

                            if titleIsInLyrics == False:
                                exactTitleCount += 1
                                titleIsInLyrics = True

#now do the percentage
print("# of songs that have lyrics using their titles: %i" % exactTitleCount)
print("# of songs in total: %i" % titleCount)
percentage = exactTitleCount / (titleCount * 1.0)
print("Percent of songs that have their titles in them: ")
print("%0.2f" % percentage)
