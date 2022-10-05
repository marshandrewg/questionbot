import logging
from pprint import pformat
import json
json_file_path  = "./questionnaires/choices.json"
logging.basicConfig(level=logging.DEBUG)


from slack_bolt import App

# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
app = App()

# Add functionality here
@app.action("multi_static_select-action")
def handle_some_action(ack, event, say, body, logger):
    # ack()
    logger.info(pformat(body))
    logger.info("Event info")
    logger.info(pformat(body['actions'][0]['selected_options']))
    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
        print(contents)
        result = app.client.users_info(
        user=body['user']['id']
        )
        logger.info(pformat(result))
        say(f"What's up? {body['user']['username']}", blocks=contents['blocks'])
        say(f"{result['user']['profile']['image_512']}")
        say(f"{body['actions'][0]['selected_options']}")
    ack()

@app.event("app_mention")
def event_test(event, body, say, logger):
    logger.info(pformat(body))
    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
        print(contents)
        result = app.client.users_info(
        user=event['user']
        )
        logger.info(pformat(result))
        say(f"What's up? ${event['user']}")
        say(f"What's up? ${event['user']}", blocks=contents['blocks'])
 

if __name__ == "__main__":
    app.start(3000)  # POST http://localhost:3000/slack/events