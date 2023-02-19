import openai
import csv
import yaml
import utils
import dotenv
import os

dotenv.load_dotenv()

# yaml_path = 'config.yaml'
# yaml_path = '.env'
# cfg       = utils.open_config_file(yaml_path)
cfg = os.getenv('OpenAI_API_KEY')
print(cfg)