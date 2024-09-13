import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")


def process_animal_data():
    # Read the JSON file
    with open('animals_data.json', 'r') as f:
        data = json.load(f)

    # Generate a string with the animals' data
    animal_info = ''
    for animal in data:
        name = animal.get('name')
        characteristics = animal.get('characteristics')
        locations = animal.get('locations')

        if name:
            animal_info += f"Name: {name}\n"

        if characteristics:
            diet = characteristics.get('diet')
            type_ = characteristics.get('type')
            if diet:
                animal_info += f"Diet: {diet}\n"
            if type_:
                animal_info += f"Type: {type_}\n"

        if locations:
            animal_info += f"Location: {locations[0]}\n"

        animal_info += "\n"
    # Read the HTML template file
    with open('animals_template.html', 'r') as f:
        html_template = f.read()

    # Replace __REPLACE_ANIMALS_INFO__ with the generated string
    html_output = html_template.replace('__REPLACE_ANIMALS_INFO__', animal_info)

    # Write the new HTML content to a new file
    with open('animals.html', 'w') as f:
        f.write(html_output)

# Call the function to process the data
process_animal_data()