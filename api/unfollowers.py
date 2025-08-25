# install instaloader: pip install instaloader
import instaloader
import os

def handler(request):
    username = os.environ.get("IG_USERNAME")
    password = os.environ.get("IG_PASSWORD")

    L = instaloader.Instaloader()
    try:
        L.login(username, password)
        return {"status": "success", "message": "Login berhasil!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
