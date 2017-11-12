# -*- coding: utf-8 -*-


from sentiment import analyze_sentiment, analyze_subjectivity
import requests
import re
from numpy import mean


DASH_SUBREDDIT = 'https://www.reddit.com/r/dashpay/'
LITECOIN_SUBREDDIT = 'https://www.reddit.com/r/litecoin/'
MONERO_SUBREDDIT = 'https://www.reddit.com/r/Monero/'
BITCOIN_SUBREDDIT = 'https://www.reddit.com/r/Bitcoin/'
BITCOIN_CASH_SUBREDDIT = 'https://www.reddit.com/r/Bitcoincash/'
ETHEREUM_SUBREDDIT = 'https://www.reddit.com/r/ethereum/'
LISK_CASH_SUBREDDIT = 'https://www.reddit.com/r/Lisk/'
AUGUR_CASH_SUBREDDIT = 'https://www.reddit.com/r/Augur/'
NEO_SUBREDDIT = 'https://www.reddit.com/r/NEO/'
STEEM_SUBREDDIT = 'https://www.reddit.com/r/steem/'
ETHEREUM_CLASSIC_SUBREDDIT = 'https://www.reddit.com/r/EthereumClassic/'
DOGECOIN_CLASSIC_SUBREDDIT = 'https://www.reddit.com/r/dogecoin/'


def get_titles(subreddit_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get(subreddit_url, headers=headers)
    res.raise_for_status()
    raw_text = res.text
    titles = re.findall('<a class="title.+?>(.+?)<', raw_text)
    return titles


def average_sentiment(text, ignore_zeros=True, negative_only=False):
    if negative_only:
        return mean([x for x in [analyze_sentiment(line) for line in text] if x < 0])
    if ignore_zeros:
        return mean([x for x in [analyze_sentiment(line) for line in text] if x != 0])
    return mean([analyze_sentiment(line) for line in text])


def average_subjectivity(text, ignore_zeros=True, negative_only=False):
    if negative_only:
        return mean([x for x in [analyze_subjectivity(line) for line in text] if x < 0])
    if ignore_zeros:
        return mean([x for x in [analyze_subjectivity(line) for line in text] if x != 0])
    return mean([analyze_subjectivity(line) for line in text])


def full_analysis(currency_name, subreddit_url):
    titles = get_titles(subreddit_url)
    sentiment = average_sentiment(titles)
    subjectivity = average_subjectivity(titles)

    print currency_name + ":"
    print "Sentiment:", sentiment
    print "Subjectivity:", subjectivity
    print




if __name__ == '__main__':
    full_analysis("Dash", DASH_SUBREDDIT)
    full_analysis("Litecoin", LITECOIN_SUBREDDIT)
    full_analysis("Monero", MONERO_SUBREDDIT)
    full_analysis("Bitcoin", BITCOIN_SUBREDDIT)
    full_analysis("Bitcoin Cash", BITCOIN_CASH_SUBREDDIT)
    full_analysis("Lisk", LISK_CASH_SUBREDDIT)
    full_analysis("Augur", AUGUR_CASH_SUBREDDIT)
    full_analysis("Neo", NEO_SUBREDDIT)
    full_analysis("Steem", STEEM_SUBREDDIT)
    full_analysis("Ethereum", ETHEREUM_SUBREDDIT)
    full_analysis("Ethereum Classic", ETHEREUM_CLASSIC_SUBREDDIT)
