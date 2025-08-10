
import requests
def message_sender(message:str,webhook_url:str)->None:
    """
    send message to teams
    """
    message = {
    "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "contentUrl": None,
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": message,
                            "wrap": True
                        }
                    ]
                }
            }
        ]
    }
    response = requests.post(webhook_url, json=message)

    if response.status_code in [200,202]:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")