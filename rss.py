#!/usr/bin/env python3
import feedparser
import sys

#feedUrl = "https://status.aws.amazon.com/rss/ec2-eu-west-1.rss"
def feedurl():
    if len(sys.argv) == 1:
        feedurl = input("Please Enter The RSS link: ")
    else:
        feedurl = sys.argv[1]
    return feedurl


def feeds_gets(feed_url):
    data = feedparser.parse(feed_url)
    print("\n----Chanel Details----")
    print(f"Channel Title: {data.feed.title}")
    print(f"Channel Description: {data.feed.description}")
    return(data)



def main():
    feed_url = feedurl()
    data = feeds_gets(feed_url)
    print("\n----Entries----")
    for i in range((len(data.entries))):
        items = data.entries[i]
        print(f"\n-----Entry {i+1}-----")
        print(f"Title: {items.title}")
        print(f"Description: {items.description}")
        print(f"Link: {items.link}")

if __name__ == "__main__":
    main()
