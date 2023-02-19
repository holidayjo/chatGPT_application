import openai
import csv
import yaml
import utils

yaml_path = r'blog_automation/config.yaml'
cfg       = utils.open_config_file(yaml_path)
# print(cfg)

openai.api_key = cfg['OpenAI_API_KEY']

word = input('Enter a word: ')

#%% Generating 10 articles using OpenAI's GPT-3
generated_articles = []
for i in range(10):
    response = openai.Completion.create(engine      = 'text-davinci-002',
                                        prompt      = f'Write an article about {word}',
                                        max_tokens  = 1024,
                                        n           = 1,
                                        stop        = None,
                                        temperature = 0.5)
    article = response['choices'][0]['text'].strip()

    generated_articles.append(article)


# print(generated_articles)

#%% Saving the articles to a csv file
with open("blog_automation/" + f"{word}.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "article"])
    for article in generated_articles:
        title = f"{word} article {generated_articles.index(article) + 1}"
        writer.writerow([title, article])
print("Saved successfully!")