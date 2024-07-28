import requests, uuid, json
from better_profanity import profanity

def translation(text,lang):
    # Add your key and endpoint
    key = "998d581023794ab58fe6e4fdb3a6fa24"
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = "westus2"

    path = '/translate'
    constructed_url = endpoint + path

    if lang == "Tamil":
        params = {
        'api-version': '3.0',
        'from': 'ta',
        'to': ['en'],
    }
            
    elif lang == "English":
        params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['ta'],
    }


    text= profanity.censor(text)
   
   

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)

    if request.status_code == 200:
        response = request.json()

    # Extract the translated text from the JSON response
        try:
            translated_text = response[0]['translations'][0]['text']
            return translated_text
        except (IndexError, KeyError) as e:
            print(f"Error extracting translated text: {e}")
    else:
        print(f"Failed to get a successful response. Status code: {response.status_code}")
  

    