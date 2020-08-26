import json, configparser
from typing import Union

config_path = "config/config.ini"

def main():
    config = load_config(config_path)
    cms_config = load_cms_config(config["cool_config"]["cms_config"])
    print(cms_config)

def load_config(file_path: str):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def load_cms_config(file_path: str):
    with open(file_path, 'r') as json_payload:
        return json.load(json_payload)

if __name__ == "__main__":
    main()