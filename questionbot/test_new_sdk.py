import os
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
json_file_path  = "./questionnaires/choices.json"
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


try:
    with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())
     print(contents)
    #  contents.blocks.options[0]
     response = client.chat_postMessage(channel='#random', text= "beep", blocks=contents['blocks'])
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")