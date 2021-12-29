import sys
import utils
import praw

reddit = praw.Reddit(client_id='CLIENT_ID',
                    client_secret='CLIENT_SECRET',
                    user_agent='USER_AGENT')

def redditScraper(subReddit, amountOfPosts=None, topOfWhat='week',Path=None):
    print ("Grabing posts from r/" + subReddit)
    print ("")
    for submission in reddit.subreddit(subReddit).top(topOfWhat, limit=amountOfPosts):
        try:
            video_url: str = submission.media["reddit_video"]["fallback_url"]
            print(video_url)
            Title = submission.title[:100].rstrip() + ".mp4"
            str(Title)
            print(Title)
            Title=Title.replace(" ","_")
            # generate audio link be replacing the DASH_{video_size} by "audio".
            # Thus DASH_640 becomes DASH_audio

            # make simple splits to seperate parts of the URL
            left = video_url.split("DASH")[0]
            right = video_url.split("?")[-1]
            middle = "DASH_audio.mp4"

            audio_url = f"{left}{middle}?{right}"

            # download both audio and video

            # video_url = "https://v.redd.it/wtxu0waz27b61/DASH_360.mp4?source=fallback"
            # audio_url = "https://v.redd.it/wtxu0waz27b61/DASH_audio.mp4?source=fallback"

            print("downloading video")
            utils.download(video_url, Path+"_"+Title)
            try:
                print("downloading audio")
                utils.download(audio_url, Path+r"audio.mp4")
            except Exception:
                print("no audio available for the video, file saved to"+Title+"_n")
                sys.exit(0)

            if not utils.check_exec():
                print("ffmpeg is not on PATH, please install or add it to PATH")
                sys.exit(0)

            # merge audio and video to a single file
            
            utils.merge_audio_video(Path+"_"+Title, Path+r"audio.mp4",Path+Title)            
        except:
            pass