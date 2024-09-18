import requests
#my_api_key = "G+cGZpp1wLxy0izuFRuNuw==EKjbtSuWSid8Q1nS"
from dotenv import load_dotenv
import os
load_dotenv()
my_api_key = os.getenv("API_KEY")
def fetch_data(animal_name):
    input_user = animal_name
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(input_user)
    response = requests.get(api_url, headers={'X-Api-Key': my_api_key})
    data = response.json()
    return data
