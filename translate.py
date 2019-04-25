# -*- coding: utf-8 -*-
from credentials import key_1
import requests
import uuid
import random

subscriptionKey = key_1

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
    # Afrikaans
    elif value == 1:
        return 'af'
    # Arabic
    elif value == 2:
        return 'ar'
    # Bangla
    elif value == 3:
        return 'bn'
    # Bosnian (Latin)
    elif value == 4:
        return 'bs'
    # Bulgarian
    elif value == 5:
        return 'bg'
    # Cantonese (Traditional)
    elif value == 6:
        return 'yue'
    # Catalan
    elif value == 7:
        return 'ca'
    # Chinese Simplified
    elif value == 8:
        return 'zh-Hans'
    # Chinese Traditional
    elif value == 9:
        return 'zh-Hant'
    # Croatian
    elif value == 10:
        return 'hr'
    # Czech
    elif value == 11:
        return 'cs'
    # Danish
    elif value == 12:
        return 'da'
    # Dutch
    elif value == 13:
        return 'nl'
    # Estonian
    elif value == 14:
        return 'et'
    # Fijian
    elif value == 15:
        return 'fj'
    # Filipino
    elif value == 16:
        return 'fil'
    # Finnish
    elif value == 17:
        return 'fi'


def translate_text(language_to, translate_text):
    params = '&to=' + language_to
    constructed_url = base_url + path + params

    body = [{
        'text': translate_text
    }]

    request = requests.post(constructed_url, headers=headers, json=body)
    return request.json()[0]['translations'][0]['text']


def generate_random_nums(size):
    while True:
        retval = random.sample(range(0, 17), size)
        # If there are no duplicates in the array and the first/last language isn't english, break
        if len(retval) == len(set(retval)) and not retval[0] == 0 and not retval[size - 1] == 0:
            break
    return retval


def get_translated_tweet(text):
    output = text
    # Generate numbers to translate to each language
    translate_nums = generate_random_nums(10)
    for i in range(len(translate_nums)):
        output = translate_text(get_language_dir(translate_nums[i]), output)
    # Translate back to English
    output = translate_text(get_language_dir(0), output)
    return output
