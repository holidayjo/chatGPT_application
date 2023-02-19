import utils

words = "How to lower blood sugar levels."

generated_articles = utils.article_generator(words)
utils.saving_csv(generated_articles)

