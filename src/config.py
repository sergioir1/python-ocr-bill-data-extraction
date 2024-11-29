import os
import json
from pathlib import Path

_DIRNAME = Path(__file__).resolve().parent.parent

class Configuration:
    _instance = None

    def __new__(cls, config_file=os.path.join(_DIRNAME, "data\\config", 'config.json')):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            cls._instance._load_configuration(config_file)
        return cls._instance

    def _load_configuration(self, config_file):
        with open(config_file, 'r') as file:
            self.config = json.load(file)

    def get(self, key):
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, None)
            if value is None:
                break
        return value

# Instancia global
cfg = Configuration()
