import csv
import requests
import json
import utils

yaml_path = r'blog_automation/config.yaml'
cfg       = utils.open_config_file(yaml_path)
# print(cfg)

access_token = cfg