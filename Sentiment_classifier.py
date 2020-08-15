projectTwitterDataFile = open("project_twitter_data.csv","r")
resultingDataFile = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(str1):
    for char in punctuation_chars:
        str1=str1.replace(char,'')
    return str1

# lists of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(str3):
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
            
def get_neg(str3):
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
