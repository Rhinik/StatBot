import json

class VkError(Exception):
    """
    For not successful requests
    """

    def __init__(self, text, description):
        self.text = f'{text}\n{str(json.dumps(description, sort_keys=True, indent=4))}'
