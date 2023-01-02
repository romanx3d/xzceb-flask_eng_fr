'''
translator mudule
'''

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import ApiException

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''eng to french'''
    try:
        result = language_translator.translate(
        english_text, model_id='en-fr').get_result()
        return result['translations'][0]['translation']
    except ApiException as ex:
        if ex.code==400: return "null input"

def french_to_english(french_text):
    '''french to eng'''
    try:
        result = language_translator.translate(
        french_text, model_id='fr-en').get_result()
        return result['translations'][0]['translation']
    except ApiException as ex:
        if ex.code==400: return "null input"
