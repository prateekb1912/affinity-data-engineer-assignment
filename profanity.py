import re
from string import punctuation

TWEETS_FILE_PATH = 'tweets.txt'
SLURS_FILE_PATH = 'slurs.txt'

def get_slurs_list(slurs_file_path: str) -> list:
    """
        Reads the text file containing all slur words and converts into a list

        Parameters:
            - slurs_file_path (str): Path of the slurs file to be read
        
        Returns:
            - A list of all slur words present in the text file
    """
    slurs_list = []
    with open(slurs_file_path, 'r') as sf:
        for slur in sf.readlines():
            slur = slur.strip()
            slurs_list.append(slur)

    return slurs_list

SLURS_LIST = get_slurs_list(SLURS_FILE_PATH)

def get_tweets_list(tweets_file_path: str) -> list:
    """
        Reads the text file containing all tweets and converts into a list cleaned and tokenized
        Each raw tweet is passed to the tokenize_raw_tweet function to get the tokens

        Parameters:
            - tweets_file_path (str): Path of the tweets file to be read
        
        Returns:
            - A list of list of tokens for all the tweets
    """
    tweets = []
    with open(tweets_file_path, 'r') as f:
        for raw_tweet in f:
            tweets.append(raw_tweet)
    
    return tweets

def tokenize_raw_tweet(raw_tweet: str) -> list:
    """ 
    Clean and tokenize a single tweet

    Parameters: 
        - raw_tweet (str): The tweet in string form to be tokenized
    
    Returns:
        - A list of tokens extracted from the tweet
    """

    # Strip redundant whitespace around
    raw_tweet = raw_tweet.strip()

    # Remove punctuations 
    raw_tweet = raw_tweet.translate(str.maketrans('', '', punctuation))

    # Split into tokens of lowercase words
    tokens = raw_tweet.lower().split()
    
    return tokens


def calculate_profanity_ratio(raw_tweet: str) -> float:
    """
    
    Calculates the profanity ratio for each tweet after cleaning and tokenizing

    Parameters:
        - raw_tweet (str): A string representing a raw tweet
    
    Returns:
        - The profanity ratio for the tweet as a float representing the percentage
    
    """

    tokens = tokenize_raw_tweet(raw_tweet)
    
    sum = 0
    n = len(tokens)

    for word in tokens:
        if word in SLURS_LIST:
            sum += 1
    
    return sum/n

def main():

    tweets_list = get_tweets_list(TWEETS_FILE_PATH)

    ratios = []

    for tweet in tweets_list:
        ratio = calculate_profanity_ratio(tweet)
        ratios.append(ratio)

    
    # Write the results to a new text file
    with open('profanity_results.txt', 'w') as pf:
        for ratio in ratios:
            pf.write(f'{ratio:.2f}\n')

if __name__ == '__main__':
    main()