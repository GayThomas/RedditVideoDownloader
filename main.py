import redditscrapper

def mainDownload():
    subredditList = ['SUBREDDIT NAME', 'SUBREDDIT NAME', 'SUBREDDIT_NAME', 'SUBREDDIT_NAME', 'SUBREDDIT_NAME', 'SUBREDDIT_NAME', 'SUBREDDIT_NAME', 'SUBREDDIT_NAME']
    for subreddit in subredditList:
        redditscrapper.redditScraper(subreddit, amountOfPosts=25,topOfWhat='week',Path='PATH')
    print("-----END-----")
if __name__ == "__main__":
    mainDownload()
