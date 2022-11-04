template_filepath = 'questionnaires/question_template.json'
import json

def convert_question_to_slack_block(question):
    question_obj = {}
    question_obj['blocks'] = []
    with open(template_filepath, 'r') as j:
        contents = json.loads(j.read())
        print(json.dumps(contents, indent=4))
        contents['blocks'][0]['text']['text'] = "beep"
        contents['blocks'][0]['accessory']['options'][0]['text']['text'] = "blart"
        contents['blocks'][0]['accessory']['options'][1]['text']['text'] = "dart"
        contents['blocks'][0]['accessory']['options'][2]['text']['text'] = "chart"
        contents['blocks'][0]['accessory']['options'][3]['text']['text'] = "paul"
        print(json.dumps(contents, indent=4))
        json

def main():
    with open('questionnaires/q1.json', 'r') as f:
        question_json = json.loads(f.read())

