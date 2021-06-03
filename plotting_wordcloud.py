import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud

# Reading dataset
tweets_df = pd.read_csv("C:/Users/nic/Documents/OUR_Project/Code/tweets.csv", skiprows=lambda x: x % 2)

print(tweets_df)
print(tweets_df.info())
print(tweets_df.describe())

# Getting length of the messages
tweets_df['length_of_text'] = tweets_df['tweet_text'].apply(len)

print(tweets_df)

# Plot histogram for length of tweet texts
tweets_df['length_of_text'].plot(bins=100, kind='hist')

sentences = tweets_df['tweet_text'].tolist()

sentences_as_one_string = " ".join(sentences)

# Plot wordcloud
plt.figure(figsize=(10,10))
plt.imshow(WordCloud().generate(sentences_as_one_string))
plt.show()
