import utils
import pandas as pd

# Pick the topic sentence.```
words = "How to lower blood sugar levels."


generated_articles = utils.article_generator(words, max_tokens=2048)
# print(generated_articles)
# utils.saving_csv(words, generated_articles)
translated = utils.translator(generated_articles)
# print(translated)

utils.posting_tistory(title=words, content=translated)

