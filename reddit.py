import praw
import os
from gtts import gTTS

reddit = praw.Reddit(
    client_id="1IN4RVKjDjkxPwEHL6XJLg",
    client_secret="tO5UgY60LMpS7pYC_R9_WxybL-lElA",
    user_agent="web:myredditapp:v1 (by u/epo_o)",
)

language = "en"
submissions = []
for i, submission in enumerate(reddit.subreddit("AmItheAsshole").hot(limit=10)):
    print(i, submission.title)
    submissions.append(submission)
while True:
    ans = input("Pick post: ")
    ans = int(ans)

    myText = submissions[ans].title + " " + submissions[ans].selftext
    print(myText)
    mp3 = gTTS(text=myText, lang=language, tld="ca", slow=False)
    mp3.save("text.mp3")
    print("**SAVED**")






# print(submission.selftext)
# print(submission.url)