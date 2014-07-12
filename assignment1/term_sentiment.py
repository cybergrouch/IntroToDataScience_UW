import sys
import json
import re

def hw():
    # 1. Read in the sentiment file into a dictionary (sentiment_dict)
    # 1.1 Prepare another dictionary of words not appearing in the sentiment_dict (non_sentiment_dict)
    # 2. Read the tweeter feed line by line
    # 2.1. For each line, convert it into a JSON object
    # 2.2. Filter the line if it is a processeable tweet
    # 2.3. Break down the tweet text into its component words
    # 2.3.1. Create a dictionary of non sentiment words for that tweet (tweet_non_sentiment_dict)
    # 2.3.2. Create a variable to store the aggreate sentiment from sentiment words for the tweet (aggregate_score)
    # 2.3.3. Create a variable to count the number of sentiment words (sentiment_word_count)
    # 2.4. For each of the words in the text
    # 2.4.1. If the word is a sentiment word (from sentiment_dict)
    # 2.4.1.1. get the word score from the tweet (from sentiment_dict)
    # 2.4.1.2. increment aggregate_score with the word score
    # 2.4.1.3. aggregate sentiment_word_count for that tweet text
    # 2.4.2. If the word is not a sentiment word
    # 2.4.2.1. Add the word in the tweet_non_sentiment_dict with its count of occurence in the tweet
    # 2.5. After processing all the words in the tweet, filter out cases when there are no sentiment words
    # 2.5.1. Compute the sentiment_score for the tweet text by this formula:
    #           sentiment_score = aggregate_score / sentiment_word_count
    # 2.5.2. For each tweet_non_sentiment_dict entry
    # 2.5.2.1. Compute the tweet_non_sentiment_word_score as follows:
    #             tweet_non_sentiment_word_score =  tweet_non_sentiment_word.get("count") * sentiment_score
    # 2.5.2.2. If the tweet_non_sentiment_word is in the non_sentiment_dict
    # 2.5.2.2.1. Get the value associated with the tweet_non_sentiment_word from non_sentiment_dict (non_sentiment_score)
    # 2.5.2.2.2. Sum non_sentiment_score and tweet_non_sentiment_word_score and store back into the non_sentiment_dict
    # 2.5.2.3. If the tweet_non_sentiment_word is NOT in the non_sentiment_dict 
    # 2.5.2.3.1. Store tweet_non_sentiment_word into non_sentiment_dict with tweet_non_sentiment_word_score

    
    # 1. Read in the sentiment file into a dictionary (sentiment_dict)
    afinnfile = open(sys.argv[1])
    sentiment_dict = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.lower().split("\t")  # The file is tab-delimited. "\t" means "tab character"
        sentiment_dict[term] = int(score)  # Convert the score to an integer.
    afinnfile.close()
    
    # 1.1 Prepare another dictionary of words not appearing in the sentiment_dict (non_sentiment_dict)
    non_sentiment_dict = {}  

    #print scores.items() 
    # Print every (term, score) pair in the dictionary
    #print 'Hello, world!'
    
    # 2. Read the tweeter feed line by line
    tweet_file = open(sys.argv[2])
    count = 1
    for line in tweet_file:
        # 2.1. For each line, convert it into a JSON object
        json_line = json.loads(line.lower())
        # 2.2. Filter the line if it is a processeable tweet
        if "text" in json_line:
            # 2.3. Break down the tweet text into its component words
            #words = re.findall(r"[\w']+|[.,!?;]", json_line.get("text"))
            #words = json_line.get("text").split(" ,")
            #words = words.split(',')
            words = re.split('; |, |\s+|\.|!|:', json_line.get("text"))
            
            # 2.3.1. Create a dictionary of non sentiment words for that tweet (tweet_non_sentiment_dict)
            tweet_non_sentiment_dict = {}
            # 2.3.2. Create a variable to store the aggreate sentiment from sentiment words for the tweet (aggregate_score)
            aggregate_score = 0
            # 2.3.3. Create a variable to count the number of sentiment words (sentiment_word_count)
            sentiment_word_count = 0
        
            # 2.4. For each of the words in the text
            for word in words:
                # 2.4.1. If the word is a sentiment word (from sentiment_dict)                
                if word in sentiment_dict:
                    # 2.4.1.1. get the word score from the tweet (from sentiment_dict)                    
                    # 2.4.1.2. increment aggregate_score with the word score                    
                    aggregate_score = aggregate_score + sentiment_dict.get(word)
                    # 2.4.1.3. aggregate sentiment_word_count for that tweet text
                    sentiment_word_count = sentiment_word_count + 1
                # 2.4.2. If the word is not a sentiment word
                else:
                    # 2.4.2.1. Add the word in the tweet_non_sentiment_dict with its count of occurence in the tweet
                    if word in tweet_non_sentiment_dict:
                        tweet_non_sentiment_dict[word] = tweet_non_sentiment_dict.get(word) + 1
                    else:
                        tweet_non_sentiment_dict[word] = 1
            
            # 2.5. After processing all the words in the tweet, filter out cases when there are no sentiment words
            if sentiment_word_count == 0:
                continue
            
            # 2.5.1. Compute the sentiment_score for the tweet text by this formula:
            #           sentiment_score = aggregate_score / sentiment_word_count
            sentiment_score = aggregate_score / sentiment_word_count 
            
            # 2.5.2. For each tweet_non_sentiment_dict entry (tweet_non_sentiment_word)
            for tweet_non_sentiment_word in tweet_non_sentiment_dict:    
                # 2.5.2.1. Compute the tweet_non_sentiment_word_score as follows:
                #             tweet_non_sentiment_word_score =  tweet_non_sentiment_word.get("count") * sentiment_score
                tweet_non_sentiment_word_score =  tweet_non_sentiment_dict.get(tweet_non_sentiment_word) * sentiment_score
                
                # 2.5.2.2. If the tweet_non_sentiment_word is in the non_sentiment_dict
                if tweet_non_sentiment_word in non_sentiment_dict:
                    # 2.5.2.2.1. Get the value associated with the tweet_non_sentiment_word from non_sentiment_dict (non_sentiment_score)
                    non_sentiment_score = non_sentiment_dict.get(tweet_non_sentiment_word) 
                    # 2.5.2.2.2. Sum non_sentiment_score and tweet_non_sentiment_word_score and store back into the non_sentiment_dict
                    non_sentiment_dict[tweet_non_sentiment_word] = non_sentiment_score + tweet_non_sentiment_word_score
                # 2.5.2.3. If the tweet_non_sentiment_word is NOT in the non_sentiment_dict 
                else:
                    # 2.5.2.3.1. Store tweet_non_sentiment_word into non_sentiment_dict with tweet_non_sentiment_word_score
                    non_sentiment_dict[tweet_non_sentiment_word] = tweet_non_sentiment_word_score
    tweet_file.close()
    
    for non_sentiment_word_in_dict in sorted(non_sentiment_dict):
        print non_sentiment_word_in_dict + "\t" + str(non_sentiment_dict.get(non_sentiment_word_in_dict))
    
def lines(fp):
    print str(len(fp.readlines()))

def main():
    hw()
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
