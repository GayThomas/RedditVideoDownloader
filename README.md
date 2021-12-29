# RedditVideoDownloader
## Intoduction
I made this program in order to download multiple videos from Reddit 

From this program you can choose subreddits from where you want to download videos, the number of posts you want to download videos from and if you want to have the best posts of the day/week/month/year/all

## Installation
1. Make sure to have ffmpeg and the packages used in utils.py and redditscraper.py installed on your computer

2. You will need to create an app here : https://www.reddit.com/prefs/apps

3. Change this line in redditscraper.py with your id and secret

>reddit = praw.Reddit(client_id='CLIENT_ID',
  client_secret='CLIENT_SECRET',
  user_agent='USER_AGENT')
  
4. Change inside of main.py the subreddits from where you want to download the videos and the path where you want the videos to be downloaded

5. You will Need to lauch the main.py file from the directory in which ffmpeg is installed

6. Wait for your videos to be downloaded (-:
