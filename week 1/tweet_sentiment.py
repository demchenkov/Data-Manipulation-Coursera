import sys
import json
import re


def lines(fp):
    return fp.readlines()


def main():
    sent_file = open(sys.argv[1])
    lines_sent_file = lines(sent_file)
    scores = {}  
    for line in lines_sent_file:
        term, score = line.split("\t")  
        scores[term] = int(score)  

    tweet_file = open(sys.argv[2])
    lines_tweet_file = lines(tweet_file)
    for line in lines_tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            text = tweet["text"]
            splitted_text = re.split(r"[\s\.,\?\:]+", text)
            sentiment = 0

            for word in splitted_text:
                if word in scores:
                    sentiment = sentiment + scores[word]

            print(sentiment)


if __name__ == '__main__':
    main()
