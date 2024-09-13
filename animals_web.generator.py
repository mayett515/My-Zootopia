import json


def generate_animal_html(animal_data):
    html = '<li class="cards__item">'

    name = animal_data.get('name')
    characteristics = animal_data.get('characteristics')
    locations = animal_data.get('locations')

    if name:
        html += f"Name: {name}<br/>"

    if characteristics:
        diet = characteristics.get('diet')
        type_ = characteristics.get('type')
        if diet:
            html += f"Diet: {diet}<br/>"
        if type_:
            html += f"Type: {type_}<br/>"

    if locations:
        html += f"Location: {locations[0]}<br/>"

    html += '</li>'
    return html


def process_animal_data():
    # Read the JSON file
    with open('animals_data.json', 'r') as f:
        data = json.load(f)

    # Generate HTML content for animals
    animal_html = ''
    for animal in data:
        animal_html += generate_animal_html(animal)

    # Read the HTML template file
    with open('animals_template.html', 'r') as f:
        html_template = f.read()

    # Replace __REPLACE_ANIMALS_INFO__ with the generated HTML
    html_output = html_template.replace('__REPLACE_ANIMALS_INFO__', animal_html)

    # Write the new HTML content to a new file
    with open('animals.html', 'w') as f:
        f.write(html_output)


# Call the function to process the data
process_animal_data()