import requests
from datetime import datetime
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

WEBHOOK_URL = "https://-----tech.webhook.office.com/webhookb2/2f673170-77ca-4b22-a43c-bb8022319812@c6c2189d-ae50-48c2-9c8a-6af3d168faa7/IncomingWebhook/d404960b64e64fe9862df422ff4c1f7a/e59606c5-5871-4e9e-beea-3720c7485537/V2Qedo_jzxm1P3Bb1jfDGbtephJneYa0xYFoIX4zB1-_k1"

message = {
    "text": f"✅ ----- automation completed at {datetime.now().strftime('%I:%M %p on %A, %B %d')}."
}

try:
    response = requests.post(WEBHOOK_URL, json=message)
    if response.status_code == 200:
        print("📨 Teams notification sent.")
    else:
        print(f"❌ Failed to send message: {response.status_code}, {response.text}")
except Exception as e:
    print(f"❌ Error sending Teams webhook: {e}")