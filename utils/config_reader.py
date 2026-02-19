import configparser
import os

def get_base_url(env):
    config = configparser.ConfigParser()
    config.read(os.path.join("config", "config.ini"))
    return config[env]["base_url"]
