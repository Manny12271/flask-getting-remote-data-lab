import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the stored URL and returns
        the raw response body (bytes).
        """
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """
        Parses the raw API response into Python data 
        (list/dict) using json.loads().
        """
        return json.loads(self.get_response_body())
