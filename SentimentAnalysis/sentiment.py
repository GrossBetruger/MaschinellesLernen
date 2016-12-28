from textblob import TextBlob
import re 

CHRISTMAS = """Remember, Christmas Day is, in the end, 
just a day. It isnt a test or a scorecard of you or your life, 
so be kind to yourself.
"""


def analyze_sentiment(text):
	blob = TextBlob(text)
	return blob.sentiment.polarity


def read_text_file(filename):
	return clear_text(open(filename).read())
	

def clear_text(text):
	return re.sub(r'[^\x00-\x7F]+',' ', text)


TRUMP_HUFFINGTON = read_text_file("donald_trump_article.txt")
OBAMA_HUFFINGTON = read_text_file("obama_huffington.txt")


if __name__=="__main__":
	print analyze_sentiment(CHRISTMAS)
	print analyze_sentiment(TRUMP_HUFFINGTON)
	print analyze_sentiment(OBAMA_HUFFINGTON)