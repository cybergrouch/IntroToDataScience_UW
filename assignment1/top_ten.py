import sys
import json
import re

def hw():
    # 1. Prepare counter dictionary
    # 1.1. Initialise frequency_histogram_dict
    # 2. Read the tweeter feed line by line
    # 2.1. For each line, convert it into a JSON object
    # 2.2. Filter the line if it is a processeable tweet
    # 2.3. Lookup the hashtags for the line 
    # 2.4. For each of the hashtag
    # 2.4.1. If the hashtag is in the frequency_history_dict
    # 2.4.1.1. get the hashtag count from frequency_history_dict (word_count_history)
    # 2.4.1.2. increment hashtag_count_history by 1
    # 2.4.1.3. store the new hashtag_count_history value back into frequency_histogram_dict[hashtag]
    # 2.4.2. If the hashtag is NOT in the frequency_history_dict
    # 2.4.2.1. Add the hashtag together with a value 1 into frequency_histogram_dict[hashtag]
    
    # 1. Prepare counter dictionary
    tweet_feed_file = open(sys.argv[1])
    
    # 1.1. Initialise frequency_histogram_dict
    frequency_histogram_dict = {}
    
    # 2. Read the tweeter feed line by line
    for line in tweet_feed_file:    
        # 2.1. For each line, convert it into a JSON object
        json_feed = json.loads(line.lower())
                
        
        # 2.2. Filter the line if it is a processeable tweet
        if json_feed.get('entities') is None:
            continue
        json_feed_entities = json_feed.get('entities')
        
        if json_feed_entities.get('hashtags') is None:
            continue

        # 2.3. Lookup the hashtags for the line 
        hashtags = json_feed_entities.get('hashtags')
        
        # 2.4. For each of the hashtag
        for hashtag in hashtags:
            tag = hashtag['text']
            
            # 2.4.1. If the hashtag is in the frequency_history_dict
            if tag in frequency_histogram_dict:
                # 2.4.1.1. get the hashtag count from frequency_history_dict (word_count_history)
                # 2.4.1.2. increment hashtag_count_history by 1
                hashtag_count_history = frequency_histogram_dict.get(tag) + 1
                # 2.4.1.3. store the new hashtag_count_history value back into frequency_histogram_dict[hashtag]
                frequency_histogram_dict[tag] = hashtag_count_history
            # 2.4.2. If the hashtag is NOT in the frequency_history_dict
            else:
                # 2.4.2.1. Add the hashtag together with a value 1 into frequency_histogram_dict[word]
                frequency_histogram_dict[tag] = 1

    tweet_feed_file.close()

    count = 1
    for hashtag_frequency in sorted(frequency_histogram_dict, key = frequency_histogram_dict.__getitem__, reverse = True):
        if count <= 10:
            print hashtag_frequency + " " + str(frequency_histogram_dict.get(hashtag_frequency))
            count = count + 1
        else:
            break
        
    
def main():
    hw()
    
if __name__ == "__main__":
    main()