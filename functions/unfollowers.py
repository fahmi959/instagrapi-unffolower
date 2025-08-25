# functions/unfollowers.py
import os
import json
from instagrapi import Client

def handler(event, context):
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

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Login berhasil",
                "user_id": client.user_id
            }),
        }
    except Exception as e:
        return {
            "statusCode": 401,
            "body": json.dumps({
                "error": f"Login gagal: {str(e)}"
            }),
        }
