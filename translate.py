# -*- coding: utf-8 -*-
from credentials import key_1
import requests
import uuid
import random
import math

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
    # Bulgarian
    elif value == 3:
        return 'bg'
    # Catalan
    elif value == 4:
        return 'ca'
    # Chinese Simplified
    elif value == 5:
        return 'zh-Hans'
    # Croatian
    elif value == 6:
        return 'hr'
    # Czech
    elif value == 7:
        return 'cs'
    # Danish
    elif value == 8:
        return 'da'
    # Dutch
    elif value == 9:
        return 'nl'
    # Estonian
    elif value == 10:
        return 'et'
    # Fijian
    elif value == 11:
        return 'fj'
    # Filipino
    elif value == 12:
        return 'fil'
    # Finnish
    elif value == 13:
        return 'fi'
    # French
    elif value == 14:
        return 'fr'
    # German
    elif value == 15:
        return 'de'
    # Greek
    elif value == 16:
        return 'el'
    # Hebrew
    elif value == 17:
        return 'he'
    # Hindi
    elif value == 18:
        return 'hi'
    # Hungarian
    elif value == 19:
        return 'hu'
    # Icelandic
    elif value == 20:
        return 'is'
    # Italian
    elif value == 21:
        return 'it'
    # Japanese
    elif value == 22:
        return 'ja'
    # Korean
    elif value == 23:
        return 'ko'
    # Lithuanian
    elif value == 24:
        return 'lt'
    # Norwegian
    elif value == 25:
        return 'nb'
    # Polish
    elif value == 26:
        return 'pl'
    # Romanian
    elif value == 27:
        return 'ro'
    # Russian
    elif value == 28:
        return 'ru'
    # Slovak
    elif value == 29:
        return 'sk'
    # Spanish
    elif value == 30:
        return 'es'
    # Swedish
    elif value == 31:
        return 'sv'
    # Vietnamese
    elif value == 32:
        return 'vi'


def translate_text_with_from(language_from, language_to, translate_text):
    params = '&from=' + language_from + '&to=' + language_to
    constructed_url = base_url + path + params

    body = [{
        'text': translate_text
    }]

    request = requests.post(constructed_url, headers=headers, json=body)
    return request.json()[0]['translations'][0]['text']


def translate_text_no_from(language_to, translate_text):
    params = '&to=' + language_to
    constructed_url = base_url + path + params

    body = [{
        'text': translate_text
    }]

    request = requests.post(constructed_url, headers=headers, json=body)
    return request.json()[0]['translations'][0]['text']


def generate_random_nums(size):
    while True:
        retval = [0]
        retval.extend(random.sample(range(0, 32), size))
        # If there are no duplicates in the array and the first/last language isn't english, break
        if len(retval) == len(set(retval)) and not retval[1] == 0 and not retval[size - 1] == 0:
            break
    return retval


def get_translated_tweet(text):
    output = text
    # Generate numbers to translate to each language
    translate_nums = generate_random_nums(15)
    for i in range(len(translate_nums) - 1):
        if i % 2 == 0:
            output = translate_text_with_from(get_language_dir(translate_nums[i]), get_language_dir(translate_nums[i + 1]), output)
        else:
            output = translate_text_no_from(get_language_dir(translate_nums[i + 1]), output)
    # Translate back to English
    output = translate_text_no_from(get_language_dir(0), output)
    return output
