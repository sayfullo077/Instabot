import random
from instagrapi import Client
from config import username, password


client = Client()
client.login(username, password)

hashtag = "programming"
comments = ["Awesome", "Great", "Nice"]

medias = []

try:
    medias = client.hashtag_medias_recent_v1(hashtag, 20)
except Exception as e:
    print("Error loading medias:", e)

for i, media in enumerate(medias):
    try:
        client.media_like(media.id)
        print(f"Liked post number {i+1} of hashtag #{hashtag}")
        if i % 5 == 0:
            client.user_follow(media.user.pk)
            print(f"Followed user {media.user.username} of post number {i+1}")
            client.media_comment(media.id, "Awesome post")
            comment = random.choice(comments)
            print(f"Commented {comment} under post number {i+1}")
            
    except Exception as e:
        print(f"Failed to like media {i+1}: {e}")