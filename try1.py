import os

# 獲取 Discord Webhook URL
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# 使用 Webhook 的部分
if WEBHOOK_URL:
    # 發送到 Discord 的邏輯
    print("Webhook URL 取得成功，發送訊息至 Discord")
else:
    print("未設定 Webhook URL，請檢查 GitHub Secrets")
