import os
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()  # hanya untuk lokal, di Vercel ENV pakai dashboard

def handler(request):
    USERNAME = os.environ.get("IG_USERNAME")
    PASSWORD = os.environ.get("IG_PASSWORD")
    TWO_FA = os.environ.get("IG_2FA")  # optional

    client = Client()
    client.delay_range = [1, 3]

    # login
    if TWO_FA:
        client.login(USERNAME, PASSWORD, verification_code=TWO_FA)
    else:
        client.login(USERNAME, PASSWORD)

    user_id = client.user_id

    # ambil followers & following
    followers_dict = client.user_followers(user_id)
    following_dict = client.user_following(user_id)

    followers_usernames = [u.username for u in followers_dict.values()]
    following_usernames = [u.username for u in following_dict.values()]

    not_following_back = [u for u in following_usernames if u not in followers_usernames]

    return {
        "statusCode": 200,
        "body": {
            "not_following_back": not_following_back,
            "followers_count": len(followers_usernames),
            "following_count": len(following_usernames)
        }
    }
