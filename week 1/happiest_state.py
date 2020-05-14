import sys
import json
import re

def lines(fp):
    return fp.readlines()

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

def main():
    sent_file = open(sys.argv[1])
    lines_sent_file = lines(sent_file)
    scores = {}
    for line in lines_sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    tweet_file = open(sys.argv[2])
    states_sentiment = {}
    lines_tweet_file = lines(tweet_file)
    for line in lines_tweet_file:
        tweet = json.loads(line)
        if "text" in tweet:
            tweet['text'].encode('ascii', 'replace')
            text = tweet["text"]
            text = text.rstrip("\n")
            splitted_text = re.split(r"[\s\.\,\?\:\!\n]+", text)
            sentiment = 0

            for word in splitted_text:
                if word in scores:
                    sentiment = sentiment + scores[word]

            user = tweet["user"]
            location = user["location"]

            for state in states.keys():
                if state in location or states[state] in location:
                    if state in states_sentiment:
                        states_sentiment[state] += sentiment
                    else:
                        states_sentiment[state] = sentiment

    happiest = ''
    for state in states_sentiment.keys():
        if happiest == '':
            happiest = state
        if states_sentiment[state] > states_sentiment[happiest]:
            happiest = state
    print(happiest)


if __name__ == '__main__':
    main()