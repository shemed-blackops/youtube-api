import json
import os

config_file_path = 'config.json'


def read_config():
    with open(config_file_path) as f:
        config = json.load(f)
        return (config['youtube']['service'], config['youtube']['version'], config['youtube']['key'])



