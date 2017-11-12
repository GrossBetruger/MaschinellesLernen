# -*- coding: utf-8 -*-


from sentiment import analyze_sentiment, clear_text
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

# blank = """<a class="title may-blank outbound" data-event-action="title" href="https://coincodex.com/crypto/dash/?view1" tabindex="1" data-href-url="https://coincodex.com/crypto/dash/?view1" data-outbound-url="https://out.reddit.com/t3_7cgnr8?url=https%3A%2F%2Fcoincodex.com%2Fcrypto%2Fdash%2F%3Fview1&amp;token=AQAAYZsIWspgFRZ8Qxy2e_sWXCrmq1B8yf3L-XHFNZzxErTt4_-R&amp;app_name=reddit.com" data-outbound-expiration="1510513505000" rel="nofollow">🚀 Dash up 25% in the last hour! Any news or just cos of BCH cooling down and money flowing back to alts?</a>"""

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


if __name__ == '__main__':
    titles = get_titles(DASH_SUBREDDIT)
    print "Dash Sentiment:", average_sentiment(titles)

    titles = get_titles(LITECOIN_SUBREDDIT)
    print "Litecoin Sentiment:", average_sentiment(titles)

    titles = get_titles(MONERO_SUBREDDIT)
    print "Monero Sentiment:", average_sentiment(titles)

    titles = get_titles(BITCOIN_SUBREDDIT)
    print "Bitcoin Sentiment:", average_sentiment(titles)

    titles = get_titles(BITCOIN_CASH_SUBREDDIT)
    print "Bitcoin Cash Sentiment:", average_sentiment(titles)

    titles = get_titles(LISK_CASH_SUBREDDIT)
    print "Lisk Sentiment:", average_sentiment(titles)

    titles = get_titles(AUGUR_CASH_SUBREDDIT)
    print "Augur Sentiment:", average_sentiment(titles)

    titles = get_titles(NEO_SUBREDDIT)
    print "Neo Sentiment:", average_sentiment(titles)

    titles = get_titles(STEEM_SUBREDDIT)
    print "Steem Sentiment:", average_sentiment(titles)

    titles = get_titles(ETHEREUM_SUBREDDIT)
    print "Ethereum Sentiment:", average_sentiment(titles)

    titles = get_titles(ETHEREUM_CLASSIC_SUBREDDIT)
    print "Ethereum classic Sentiment:", average_sentiment(titles)