import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        
        return response.content

    def load_json(self):
        results_json = GetRequester(self.url).get_response_body()
        
        converted_results = json.loads(results_json)
        
        return converted_results
