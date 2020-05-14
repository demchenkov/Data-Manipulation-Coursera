import sys
import json
from collections import Counter


def lines(fp):
    return fp.readlines()


def main():
    tweet_file = open(sys.argv[1])
    hashtags = {}
    lines_tweet_file = lines(tweet_file)
    for line in lines_tweet_file:
        tweet = json.loads(line)
        if "entities" in tweet:
            entities = tweet["entities"]
            hashtags_in_line = entities["hashtags"]

            for hashtag in hashtags_in_line:
                text = hashtag["text"]
                if text in hashtags.keys():
                    hashtags[text] += 1
                else:
                    hashtags[text] = 1

    sorted_hashtags = Counter(hashtags)
    top_ten = sorted_hashtags.most_common(10)
    for top in top_ten:
        print(top[0] + " " + str(top[1]))


if __name__ == '__main__':
    main()
