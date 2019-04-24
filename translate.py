# -*- coding: utf-8 -*-
import requests
import uuid
import json
import credentials

# If you want to set your subscription key as a string, uncomment the line
# below and add your subscription key.
subscriptionKey = credentials.key_1

base_url = 'https://api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'

headers = {
    'Ocp-Apim-Subscription-Key': subscriptionKey,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


def get_language_dir(value):
    # English
    if value == 0:
        return 'en'
    # Spanish
    elif value == 1:
        return 'es'
    # Russian
    elif value == 2:
        return 'ru'
    # Portuguese
    elif value == 3:
        return 'pt'
    # Polish
    elif value == 4:
        return 'pl'
    # Norwegian
    elif value == 5:
        return 'nb'


def translate_text(language_to, translate_text):
    params = '&to=' + language_to
    constructed_url = base_url + path + params

    body = [{
        'text': translate_text
    }]

    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()

    print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))


print(translate_text(get_language_dir(3), 'Hello world, how are you doing?'))
