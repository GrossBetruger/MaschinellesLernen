from textblob.classifiers import NaiveBayesClassifier
import json
from random import choice  

train = [
     ('I love this sandwich.', 'pos'),
     ('this is an amazing place!', 'pos'),
     ('I feel very good about these beers.', 'pos'),
     ('this is my best work.', 'pos'),
     ("what an awesome view", 'pos'),
     ('I do not like this restaurant', 'neg'),
     ('I am tired of this stuff.', 'neg'),
     ("I can't deal with this", 'neg'),
     ('he is my sworn enemy!', 'neg'),
     ('my boss is horrible.', 'neg')]


test = [
     ('the beer was good.', 'pos'),
     ('I do not enjoy my job', 'neg'),
     ("I ain't feeling dandy today.", 'neg'),
     ("I feel amazing!", 'pos'),
     ('Gary is a friend of mine.', 'pos'),
     ("I can't believe I'm doing this.", 'neg')]

def load_json(jfile):
     with open(jfile, "r") as f:
          return json.load(f)


cl = NaiveBayesClassifier(train)


positive_reviews = [x['text'] for x in load_json("good_reviews.json")]
negative_reviews = [x['text'] for x in load_json("bad_reviews.json")]
print "number of positive reviews", len(positive_reviews)
print "number of negatvie reviews", len(negative_reviews)
training_set = [(x, 'pos') for x in positive_reviews] + [(x, 'neg') for x in negative_reviews]
training_set = [choice(training_set) for i in range(len(training_set))]
print "training_set size", len(training_set)


neg_review_example = "Gosh - just hire a designer for 10 hours Flagship product with an app that's looks like an afterthought should be embarrassing for the product managers. I would be embarrassed on my resume to say I built this app for Insteon. Just hire a designer and rebuild the app - or message me and I'll design you one. I have a ton of Insteon devices at home and just absolutely hate the look and UX of this app. Also a mega embarrassment to recommend Insteon to friends. They might throw up after looking at the app."
neg_review_example2 = "Don't waste your money on Insteon Close to $1000 in equipment, and 100s of hours put into trying to get this system set up right and it still gives me headaches every day. The Insteon for Hub app itself has hardly changed since it's first debut despite numerous obvious shortcomings. At this point I am using Logitech's Harmony system to control my hub because they managed to create a better interface in a matter of months than Insteon has in several years..i swear, there can't be more than 2 people on their development team."
neg_review_example3 = "Still waiting For an interference updated to modern standards. And get rid of the stupid dial on the thermostat!"
neg_review_example4 = "Ava Bc it looks nothing like my hand.and its just stupid BC when I moved the hand on the x-ray thighs stayed in one spot and I wanted x-ray I would ask my mom to take me to the doctor this game should be deleted"
pos_review_example = "Challenging This is a great game that will challenge your mind. However, you will need a programming background or at least the ability to quickly learn how to program from scanty documentation. There are 3 distinct modes ... puzzles, robot and games. In puzzles, you must write short programs to manipulate various inputs into given outputs. Robot is a beta feature that asks you to program the movement of a virtual robot in a random maze. Games is a sandbox mode allowing you to create and share programs. Recommended."




print cl.classify("This is an amazing library!")
print cl.classify("I'm not very nice!")
print cl.classify("I'm  very nice!")

prod_cl = NaiveBayesClassifier(training_set)

print "reviews classification"
print prod_cl.classify(neg_review_example2)
print prod_cl.classify(neg_review_example)
print prod_cl.classify(neg_review_example3)
print prod_cl.classify(neg_review_example4)
print prod_cl.classify(pos_review_example)