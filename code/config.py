from json import loads
from DotDict import DotDict

def load():
    """
    Return content of config
    """
    
    with open("./code/config.json") as file:

        json_content = loads(file.read())
        return DotDict(json_content)
