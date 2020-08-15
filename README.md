# Python-Project-Sentiment-Classifier

## Problem Statement: 
> * Build a sentiment classifier, which will detect how positive or negative a tweet is.

## Project Description:
> * There are available some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet.
> * There are also available  words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

## Project Task:
### Task-1:
> - [x] Build a sentiment classifier, which will detect how positive or negative a tweet is.
```
projectTwitterDataFile = open("project_twitter_data.csv","r")
resultingDataFile = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(str1): # Function for removing Punctuation.
    for char in punctuation_chars:
        str1=str1.replace(char,'')
    return str1

# lists of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(str3): # Function for getting no of Positive words in tweet. 
    count=0
    str4=strip_punctuation(str3)
    str5=str4.lower()
    #print(str5)
    words=str5.split(' ')
    #print(words)
    for word in words:
        
        if word in positive_words:
            #print(word,count)
            count=count+1
    return count

# lists of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_neg(str3): # Function for getting no of Positive words in tweet.
    count=0
    str4=strip_punctuation(str3)
    str5=str4.lower()
    #print(str5)
    words=str5.split(' ')
    #print(words)
    for word in words:
        if word in negative_words:
            #print(word, count)
            count=count+1
    return count            
```
### Task-2:
> - [x] Create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet.
```
def writeInDataFile(resultingDataFile): # Function for generating csv file.
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  projectTwitterDataFile.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")

        
writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()
```
### Task-3:
> - [x] Produce a graph(scatter plot) of the Net Score vs Number of Retweets with Google sheets, using created csv file.
## Project Result:
> - [x] By completing all three above task we got the scatter plot between Net Score vs Number of Retweets with Google sheets which can be check out as below-
>  ![Sentiment Classifier result](/result.png)

## Project conclusion :tada::
> - [x] By Completing this project Build a sentiment classifier, which will detect how positive or negative a tweet is. By using this sentiment classifier we produce a csv file containging columns for the Number of Retweets, Number of Replies, Positive Score , Negative Score, and the Net Score for each tweet. By using this csv file we generated a scatter Plot of the Net Score vs Number of Retweets, so we can understand that how a tweet is Positive or Negative.
