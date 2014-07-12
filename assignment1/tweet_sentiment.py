import sys
import json
import re

def hw():
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.lower().split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    afinnfile.close()

    #print scores.items() 
    # Print every (term, score) pair in the dictionary
    #print 'Hello, world!'
    
    tweet_file = open(sys.argv[2])
    #count = 1
    for line in tweet_file:
        json_line = json.loads(line.lower())
        if "text" in json_line:
            words = re.findall(r"[\w']+|[.,!?;]", json_line.get("text"))
            total_score = 0
        
            #line_score = {}
            #line_score["text"] = json_line.get("text")
            #line_score["words"] = {}
            for word in words:
                if word in scores:
                    #line_score["words"][word] = scores.get(word)
                    total_score = total_score + scores.get(word)
                #else:
                    #line_score["words"][word] = 0
            
            #line_score["line"] = count
            #line_score["total_score"] = total_score
            #count = count + 1
                
            #print json.dumps(line_score, indent=4, separators=(',', ': '))
            print total_score
        else:
            print 0
    tweet_file.close()

def lines(fp):
    print str(len(fp.readlines()))

def main():
    hw()
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
