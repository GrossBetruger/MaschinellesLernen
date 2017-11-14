# -*- coding: utf-8 -*-


from sentiment import analyze_sentiment, analyze_subjectivity
import requests
import re
from numpy import mean
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring


COINGECKO_MAIN = 'https://www.coingecko.com/en'

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
RIPPLE_CLASSIC_SUBREDDIT = 'https://www.reddit.com/r/Ripple/'
TETHER_SUBREDDIT = 'https://www.reddit.com/r/Tether/'
BANCOR_SUBREDDIT = 'https://www.reddit.com/r/Bancor/'

NEXT_PAGE_PATTERN = '\?count=\d+&amp;after=[^"]+'
SECOND_NEXT_PAGE_PATTERN = '\?amp=&amp;count=\d+&amp;after=[^"]+'


def scrap_text(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.text


def get_coin_fundementals():
    raw_text = scrap_text(COINGECKO_MAIN).replace("\n", "")
    rows = re.findall("<tr>.+?</tr>", raw_text)
    for row in rows:
        # if "monero" in row:
        try:
            name = re.findall(r"crypto-symbol text-muted'>(.+?)</span>", row)[0]
            hash_algo = re.findall(r"<small>(.+?)</small>", row)[0]
            print "NAME:", name
            print "HASH ALGO:", hash_algo
            print
        except IndexError:
            pass



def parse_xml(raw):
    return bf.data(fromstring(raw))


def get_titles(subreddit_url):
    raw_text = scrap_text(subreddit_url)
    titles = re.findall('<a class="title.+?>(.+?)<', raw_text)
    next_url_suffix = re.findall(NEXT_PAGE_PATTERN, raw_text)
    next_url_suffix2 = re.findall(SECOND_NEXT_PAGE_PATTERN, raw_text)
    if next_url_suffix or next_url_suffix2:
        next_url_suffix = next_url_suffix if next_url_suffix else  next_url_suffix2
        number = int(re.findall("count=(\d+)", next_url_suffix[0])[0])
        if number > 100:
            return titles
        next_url = subreddit_url.split("?")[0] + next_url_suffix[0]
        return titles + get_titles(next_url)

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
    get_coin_fundementals()
    quit()
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
    full_analysis("Ripple", RIPPLE_CLASSIC_SUBREDDIT)
    full_analysis("Tether", TETHER_SUBREDDIT)
    full_analysis("Bancor", BANCOR_SUBREDDIT)
