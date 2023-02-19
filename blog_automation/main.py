import openai
import csv
import yaml
import utils
import dotenv
import os

dotenv.load_dotenv(verbose=True) # if there is a missing file, show the warning.

cfg = os.getenv('OpenAI_API_KEY')
print(cfg)