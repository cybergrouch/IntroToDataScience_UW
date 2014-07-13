import sys
import json
import re

def hw():
    # 1. Prepare counter dictionary
    # 1.1. Initialise frequency_histogram_dict
    # 2. Read the tweeter feed line by line
    # 2.1. For each line, convert it into a JSON object
    # 2.2. Filter the line if it is a processeable tweet
    # 2.3. Break down the tweet text into its component words
    # 2.4. For each of the words in the text
    # 2.4.1. If the word is in the frequency_history_dict
    # 2.4.1.1. get the word count from frequency_history_dict (word_count_history)
    # 2.4.1.2. increment word_count_history by 1
    # 2.4.1.3. store the new word_count_history value back into frequency_histogram_dict[word]
    # 2.4.2. If the word is NOT in the frequency_history_dict
    # 2.4.2.1. Add the word together with a value 1 into frequency_histogram_dict[word]
    
    # 1. Prepare counter dictionary
    tweet_feed_file = open(sys.argv[1])
    
    # 1.1. Initialise frequency_histogram_dict
    frequency_histogram_dict = {}
    
    # 2. Read the tweeter feed line by line
    for line in tweet_feed_file:    
        # 2.1. For each line, convert it into a JSON object
        json_feed = json.loads(line.lower())
        
        # 2.2. Filter the line if it is a processeable tweet
        if json_feed.get('text') is None:
            continue
            
        # 2.3. Break down the tweet text into its component words
        words = re.split('; |, |\s+|\.|!|:', json_feed.get("text"))
        
        # 2.4. For each of the words in the text
        for word in words:
            if not word:
                continue
            
            # 2.4.1. If the word is in the frequency_history_dict
            if word in frequency_histogram_dict:
                # 2.4.1.1. get the word count from frequency_history_dict (word_count_history)
                # 2.4.1.2. increment word_count_history by 1
                word_count_history = frequency_histogram_dict.get(word) + 1
                # 2.4.1.3. store the new word_count_history value back into frequency_histogram_dict[word]
                frequency_histogram_dict[word] = word_count_history
            # 2.4.2. If the word is NOT in the frequency_history_dict
            else:
                # 2.4.2.1. Add the word together with a value 1 into frequency_histogram_dict[word]
                frequency_histogram_dict[word] = 1

    tweet_feed_file.close()

    for word_frequency in frequency_histogram_dict:
        print word_frequency + " " + str(frequency_histogram_dict.get(word_frequency))
    
def main():
    hw()
    
if __name__ == "__main__":
    main()