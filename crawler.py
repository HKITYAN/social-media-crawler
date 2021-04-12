import os
import tweepy
import csv
import sys
import snscrape.modules.twitter as sntwitter


def crawler(source_file_dir: str) -> None:
    with open(source_file_dir, 'r') as stock_profile_list:
        data_folder_dir = os.path.dirname(source_file_dir)
        with open(os.path.join(data_folder_dir, 'tweet.csv'), 'w') as tweet_list:
            fields = ['Stock', 'Date', 'Content', 'Author']
            tweet_writer = csv.DictWriter(tweet_list, fields)
            tweet_writer.writeheader()

            rstocklist = csv.DictReader(stock_profile_list)
            next(rstocklist)

            for row in rstocklist:
                max_tweets = 10
                print(f"searching for ticker ${row['ticker']}")
                hashtag = f"${row['ticker']}"

                try:
                    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(hashtag).get_items()):
                        if i > max_tweets:
                            break
                        tweet_writer.writerow(
                            {'Stock': row['ticker'], 'Date': str(tweet.date), 'Content': tweet.content,
                             'Author': tweet.username})
                except Exception as e:  # work on python 3.x
                    print(str(e))


def main():
    source_file_dir = sys.argv[1]
    crawler(source_file_dir)


if __name__ == '__main__':
    main()
