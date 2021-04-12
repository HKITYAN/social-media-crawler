import os
import tweepy
import csv
import sys

def crawler(source_file_dir: str) -> None :
    with open(source_file_dir, 'r') as stock_profile_list:
        data_folder_dir = os.path.dirname(source_file_dir)
        with open(os.path.join(data_folder_dir, 'tweet.csv'), 'w') as tweet_list:
            fields = ['Stock', 'Date', 'Content', 'Author']
            tweetWriter = csv.DictWriter(tweet_list, fields)
            tweetWriter.writeheader()

            rstocklist = csv.DictReader(stock_profile_list)
            next(rstocklist)

            for row in rstocklist:

                tweetsPerQry = 100
                maxTweets = 1000000
                print("Searching for $" + row['ticker'])
                hashtag = "$" + row['ticker']

                try:
                    print()
                except Exception as e: # work on python 3.x
                    print(str(e))

                

                

                

def main():
    source_file_dir = sys.argv[1]
    crawler(source_file_dir)
    
if __name__ == '__main__':
    main()

