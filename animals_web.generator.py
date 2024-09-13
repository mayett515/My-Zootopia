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

  # Iterate through each animal
  for animal in data:
    print("\nName:", animal.get('name'))

    characteristics = animal.get('characteristics')
    if characteristics:
      diet = characteristics.get('diet')
      if diet:
        print("Diet:", diet)

      type_ = characteristics.get('type')
      if type_:
        print("Type:", type_)

    locations = animal.get('locations')
    if locations:
      print("Location:", locations[0])


# Call the function to process the data
process_animal_data()