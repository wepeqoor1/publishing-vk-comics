import json

class VKCodeExceptions(Exception):
    def __init__(self, message: dict):
        self.message = message

    def __str__(self):
        return f"VK API ERROR: \n{json.dumps(self.message, indent=4, sort_keys=True)}"
