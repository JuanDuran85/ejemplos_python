"""_summary_

    Using TextBlob to analyze text

"""

from textblob import TextBlob

tweets: tuple = ('I was happy with the book','thisis awful', 'Python is object oriented', 'Python is awsome')

for tw in tweets:
    print(tw)
    print(TextBlob(tw).sentiment)
    