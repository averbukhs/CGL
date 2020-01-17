import yaml

with open("config.yaml", 'r') as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

class Config(object):
    def __init__(self):
        self._config = conf

    def get_componies(self):
        if 'companies' not in self._config.keys(): 
            return None  
        return self._config['companies']
    def get_base_url(self):
        if 'base_url' not in self._config.keys():
            return None
        return self._config['base_url']