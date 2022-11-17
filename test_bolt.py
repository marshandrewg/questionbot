import logging
from pprint import pformat
import json
from dotenv import load_dotenv, find_dotenv
from slack_bolt import App
import os
import requests
import frame_picture
question_json_file_path  = "./questionnaires/choices.json"
scores_json_file_path = "./questionnaries/scores.json"
logging.basicConfig(level=logging.DEBUG)

load_dotenv()
print(os.environ)

app = App()

# Add functionality here
@app.action("multi_static_select-action")
def handle_some_action(ack, event, say, body, logger):
    chosen = []
    for choice in body['actions'][0]['selected_options']:
        chosen.append(choice['text']['text'])
    
    logger.info(pformat(body['actions'][0]['selected_options']))
    with open(question_json_file_path, 'r') as j:
        contents = json.loads(j.read())
        print(contents)
        result = app.client.users_info(
        user=body['user']['id']
        )
        logger.info(pformat(result))
        say(f"What's up? {body['user']['username']}", blocks=contents['blocks'])
        # say(f"{result['user']['profile']['image_512']}")
        say(f"{body['actions'][0]['selected_options']}")
        app.client.chat_postEphemeral(user=body['user']['id'],channel=body['channel']['id'],text=f"{chosen[0]} was correct! Currently you have ✴️ 1240 POINTS ✴️ this week. ")
    ack()

@app.event("app_mention")
def handle_app_mention_events(ack,body,logger,say,event):
    logger.info(event)
    result = app.client.users_info(
        user=event['user']
        )
    say(f"{result['user']['profile']['image_512']}")
    resp = requests.get(f"{result['user']['profile']['image_512']}")
    with open("512.png", "wb") as file: # opening a file handler to create new file 
        file.write(resp.content) # writing content to file
    frame_picture.animate_foreground()
    app.client.files_upload(file="out.gif", channels=["random"])
    ack()

@app.event("app_home_opened")
def handle_app_home_opened_events(body, logger):
    logger.info(body)

if __name__ == "__main__":
    app.start(3000)  # POST http://localhost:3000/slack/events