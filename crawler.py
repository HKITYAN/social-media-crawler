import os
import tweepy
import csv
import sys

consumer_key = "aaaaaaaaaaaa"
consumer_secret = "zzzzzzzzzzz"
access_token = "xxxxxxxxx"
access_token_secret = "yyyyyyyyyy"

def crawler(data_dir: str):
    print(data_dir)

# root_dir = os.path.dirname(os.getcwd())
# data_dir = os.path.join(root_dir, 'data')

def main():
    data_dir = sys.argv[1]
    crawler(data_dir)
    
if __name__ == '__main__':
    main()

