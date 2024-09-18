import requests
my_api_key = "G+cGZpp1wLxy0izuFRuNuw==EKjbtSuWSid8Q1nS"
def fetch_data(animal_name):
    input_user = animal_name
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(input_user)
    response = requests.get(api_url, headers={'X-Api-Key': my_api_key})
    data = response.json()
    return data