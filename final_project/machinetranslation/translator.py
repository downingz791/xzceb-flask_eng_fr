
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(english_text):
    ''' converts english text to french '''
    response = language_translator.translate(
        text=english_text,
        model_id='en-fr')
    frenchText = json.dumps(response.result['translations'][0]['translation'])
    return frenchText

def frenchToEnglish(french_text):
    ''' converts french text to english '''
    response = language_translator.translate(
        text=french_text,
        model_id='fr-en')
    englishText = json.dumps(response.result['translations'][0]['translation'])
    return englishText

english_text_input = 'Hello'
french_translation = englishToFrench(english_text_input)
print(french_translation)

french_text_input = 'Bonjour'
english_translation = frenchToEnglish(french_text_input)
print(english_translation)
