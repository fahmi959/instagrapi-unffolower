from instagrapi import Client
import os

def handler(request):
    username = os.environ.get("IG_USERNAME")
    password = os.environ.get("IG_PASSWORD")
    
    cl = Client()
    try:
        cl.login(username, password)
        profile = cl.user_info_by_username(username)
        return {
            "status": "success",
            "username": profile.username,
            "full_name": profile.full_name
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
