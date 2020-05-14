import sys
import json
import re


def lines(fp):
    return fp.readlines()


def main():
    tweet_file = open(sys.argv[1])
    count = 0
    words = {}
    lines_tweet_file = lines(tweet_file)
    for line in lines_tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            tweet['text'].encode('ascii', 'replace')
            text = tweet["text"]
            text = text.rstrip("\n")
            splitted_text = re.split(r"[\s\.\,\?\:\!\n]+", text)

            count += len(splitted_text)

            for word in splitted_text:
                if word != '':
                    if word in words:
                        words[word] += 1.0
                    else:
                        words[word] = 1.0
    for word in words.keys():
        print(word + " " + str(round(words[word] / count, 4)))


if __name__ == '__main__':
    main()
