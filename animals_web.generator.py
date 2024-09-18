import json
import requests
import data_fetcher


def serialize_animal(animal_data):
    html = '<li class="cards__item">'

    name = animal_data.get('name')
    characteristics = animal_data.get('characteristics')
    locations = animal_data.get('locations')

    if name:
        html += f'<div class="card__title">{name}</div>'

    html += '<p class="card__text">'

    if locations:
        html += f'<strong>Location:</strong> {locations[0]}<br/>'

    if characteristics:
        diet = characteristics.get('diet')
        type_ = characteristics.get('type')

        if diet:
            html += f'<strong>Diet:</strong> {diet}<br/>'

        if type_:
            html += f'<strong>Type:</strong> {type_}<br/>'

    html += '</p>'
    html += '</li>'
    return html




def process_animal_data(fetch):
    # Read the JSON file
    with open('animals_data.json', 'r') as f:
        data = json.load(f)

    # Generate HTML content for animals
    animal_html = ''
    for animal in data:
        animal_html += serialize_animal(animal)

    # Read the HTML template file
    with open('animals_template.html', 'r') as f:
        html_template = f.read()

    # Replace __REPLACE_ANIMALS_INFO__ with the generated HTML
    html_output = html_template.replace('__REPLACE_ANIMALS_INFO__', animal_html)

    # Write the new HTML content to a new file
    with open('animals.html', 'w') as f:
        f.write(html_output)

#name = "Fox"
#api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
my_api_key = "G+cGZpp1wLxy0izuFRuNuw==EKjbtSuWSid8Q1nS"
#response = requests.get(api_url, headers={'X-Api-Key': my_api_key})

def process_animal_data_new(fetched_file):
    # Read the JSON file
    data = fetched_file

    # Generate HTML content for animals
    animal_html = ''
    for animal in data:
        animal_html += serialize_animal(animal)

    # Read the HTML template file
    with open('animals_template.html', 'r') as f:
        html_template = f.read()

    # Replace __REPLACE_ANIMALS_INFO__ with the generated HTML
    html_output = html_template.replace('__REPLACE_ANIMALS_INFO__', animal_html)

    # Write the new HTML content to a new file
    with open('animals.html', 'w') as f:
        f.write(html_output)


# Call the function to process the data
#process_animal_data_new()

animal_name = input("Please enter an animal: ")
data = data_fetcher.fetch_data(animal_name)
process_animal_data_new(data)


