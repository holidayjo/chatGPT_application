import requests
import os
import dotenv
import json

dotenv.load_dotenv(verbose=True)

def translator(text):
    id = os.getenv('Papago_ID')
    pw = os.getenv('Papago_Secret')
    header = {"X-Naver-Client-Id"     : id,
              "X-Naver-Client-Secret" : pw}
    data = {'text'  : text,
            'source': 'en',
            'target': 'ko'}
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    response = requests.post(url, headers=header, data=data)
    
    if response.status_code == 200:
        output = response.json()
        output = output['message']['result']['translatedText']
        return output
    else:
        print('Error Code: ', response)

