import logging
from pprint import pformat
import json
question_json_file_path  = "./questionnaires/choices.json"
scores_json_file_path = "./questionnaries/scores.json"
logging.basicConfig(level=logging.DEBUG)


from slack_bolt import App
app = App()

# Add functionality here
@app.action("multi_static_select-action")
def handle_some_action(ack, event, say, body, logger):
    logger.info(pformat(body))
    logger.info("Event info")
    logger.info(pformat(body['actions'][0]['selected_options']))
    with open(question_json_file_path, 'r') as j:
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

if __name__ == "__main__":
    app.start(3000)  # POST http://localhost:3000/slack/events