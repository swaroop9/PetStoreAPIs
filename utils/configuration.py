import configparser
import json
import os

payload_path = os.path.abspath("utils/payload.json")
properties_path = os.path.abspath("utils//properties.ini")


def payload():
    # Opening JSON file
    with open(payload_path) as data:
        # returns JSON object as
        # a dictionary
        return json.load(data)


def getConfig():
    config = configparser.ConfigParser()
    config.read(properties_path)
    return config
