import os
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()  # lokal saja, di Vercel ENV pakai dashboard

def handler(request):
    USERNAME = os.environ.get("IG_USERNAME")
    PASSWORD = os.environ.get("IG_PASSWORD")
    TWO_FA = os.environ.get("IG_2FA")  # opsional

    client = Client()
    client.delay_range = [0.5, 1]

    try:
        if TWO_FA:
            client.login(USERNAME, PASSWORD, verification_code=TWO_FA)
        else:
            client.login(USERNAME, PASSWORD)
        # Login berhasil
        return {
            "statusCode": 200,
            "body": {"message": "Login berhasil", "user_id": client.user_id}
        }
    except Exception as e:
        # Login gagal
        return {
            "statusCode": 401,
            "body": {"error": f"Login gagal: {str(e)}"}
        }
