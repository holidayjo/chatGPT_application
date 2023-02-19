import requests
import csv
import openai
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

def article_generator(words, num_articles=1, max_tokens=2048):
    openai.api_key    = os.getenv('OpenAI_API_KEY')
    generated_article = []
    for _ in range(num_articles):
        response = openai.Completion.create(engine      = 'text-davinci-002',
                                            prompt      = f'Write an article about {words}',
                                            max_tokens  = max_tokens,
                                            n           = 1,
                                            stop        = None,
                                            temperature = 0.5)
        article = response['choices'][0]['text'].strip()
        generated_article.append(article)
    return generated_article

def saving_csv(words, generated_articles): 
    '''
    words : that the articles are about.
    '''
    with open("blog_automation/" + f"{words}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "article"])
        for article in generated_articles:
            title = f"{words} article {generated_articles.index(article) + 1}"
            writer.writerow([title, article])
    print("Saved successfully!")

def posting_tistory(title='No Tile', content='No Content'):
    print('Title =', title)
    url      = "https://www.tistory.com/apis/post/write?"
    output   = "json"
    blogName = "ossam1996"
    
    data = url
    data += "access_token=" + os.getenv('Tistory_Secret_Key') + "&"
    data += "output=" + output + "&"
    data += "blogName=" + blogName + "&"
    data += "title" + title + "&"
    data += "content=" + content + "&"
    # data += "category=vegetable"
    
    print(data)
    res = requests.post(data)
    
    

    