from json import loads


def load():
    """
    Return content of config
    """
    CONFIG_PATH = "code/config.json"

    with open(CONFIG_PATH) as file:

        json_content = loads(file.read())
        return json_content
