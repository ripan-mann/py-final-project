from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
API_KEY = 'DFN8Dwak8MqDAELfxMWALSISATYiKCNCgzaYKcQ8ypkA'
API_URL = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/f2a4e160-4c26-48ec-a446-de94080811fa'


# Prepare the Authenticator
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(API_URL)

# Translate to French
def translate_to_fr(text_to_translate):
    translation = language_translator.translate(text=text_to_translate, model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

# Translate to English
def translate_to_en(text_to_translate):
    translation = language_translator.translate(text=text_to_translate, model_id='fr-en').get_result()
    return translation['translations'][0]['translation']
