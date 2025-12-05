# Getting Remote Data Lab

This lab implements a `GetRequester` class to fetch remote JSON data and convert it into Python objects.  
It can be reused in Flask apps or any Python project that consumes APIs.

## GetRequester Class

Located in `lib/GetRequester.py`:

```python
import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        return json.loads(self.get_response_body())
Usage Example
from lib.GetRequester import GetRequester

requester = GetRequester(
    "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
)
people = requester.load_json()
print(people)