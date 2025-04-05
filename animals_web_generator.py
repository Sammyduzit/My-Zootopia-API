import sys
import data_fetcher
import data_processing


def save_to_file(file_path, content):
    """
    Write content to a file.
    :param file_path: File path destination
    :param content: String content to be written to the file
    :return: None
    :raises: SystemExit if file cannot be written
    """
    try:
        with open(file_path, "w", encoding="utf-8") as handle:
            handle.write(content)
    except IOError as e:
        sys.exit(f"Error: Could not write to file {file_path}: {e}")


def get_user_animal():
    """
    Gets animal name by user input. No empty string
    :return:
    """
    while True:
        try:
            user_animal = input("Enter animal name (or 'q' to quit): ").strip()
            if not user_animal:
                print("Please enter a name")
                continue
            if user_animal.lower() == "q":
                sys.exit("Goodbye!")

        except (EOFError, KeyboardInterrupt):
            sys.exit("Operation cancelled by user.")
        break
    return user_animal


# HTML CONTENT
def load_html_template(file_path):
    """
    Load and return HTML template content.
    :param file_path: Path to the HTML file to be loaded
    :return: HTML content as string
    :raises: SystemExit if file not found or cannot be loaded
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return handle.read()
    except FileNotFoundError:
        sys.exit(f"Error: File not found: {file_path}")
    except IOError as e:
        sys.exit(f"Error: Could not read HTML template {file_path}: {e}")


def generate_animal_card(animal_data):
    """
    Generate HTML card for a single animal.
    Silently skips any missing or None fields.
    :param animal_data: Dictionary containing animal data
    :return: HTML string with animal card infos
    """
    card = ['<li class="cards__item">']

    if animal_data.name:
        card.append(f'<div class="card__title">{animal_data.name}</div>')

    card.append('<div class="card__text">\n<ul>')

    if animal_data.taxonomy.scientific_name:
        card.append(f'<li><strong>Scientific Name:</strong> '
                    f'{animal_data.taxonomy.scientific_name}</li>')

    if animal_data.characteristics.type:
        card.append(f'<li><strong>Type:</strong> '
                    f'{animal_data.characteristics.type}</li>')

    if animal_data.characteristics.skin_type:
        card.append(f'<li><strong>Skin Type:</strong> '
                    f'{animal_data.characteristics.skin_type}</li>')

    if animal_data.locations:
        card.append(f'<li><strong>Location(s):</strong> '
                    f'{", ".join(animal_data.locations)}</li>')

    if animal_data.characteristics.habitat:
        card.append(f'<li><strong>Habitat:</strong> '
                    f'{animal_data.characteristics.habitat}</li>')

    if animal_data.characteristics.water_type:
        card.append(f'<li><strong>Water type:</strong> '
                    f'{animal_data.characteristics.water_type}</li>')

    if animal_data.characteristics.optimum_ph_level:
        card.append(f'<li><strong>Optimum ph-level:</strong> '
                    f'{animal_data.characteristics.optimum_ph_level}</li>')

    if animal_data.characteristics.nesting_location:
        card.append(f'<li><strong>Nesting location:</strong> '
                    f'{animal_data.characteristics.nesting_location}</li>')

    if animal_data.characteristics.group_behavior:
        card.append(f'<li><strong>Group behavior:</strong> '
                    f'{animal_data.characteristics.group_behavior}</li>')

    if animal_data.characteristics.diet:
        card.append(f'<li><strong>Diet:</strong> '
                    f'{animal_data.characteristics.diet}</li>')

    if animal_data.characteristics.favorite_food:
        card.append(f'<li><strong>Favorite food:</strong> '
                    f'{animal_data.characteristics.favorite_food}</li>')

    if animal_data.characteristics.prey:
        card.append(f'<li><strong>Prey:</strong> '
                    f'{animal_data.characteristics.prey}</li>')

    if animal_data.characteristics.predators:
        card.append(f'<li><strong>Predators:</strong> '
                    f'{animal_data.characteristics.predators}</li>')

    if animal_data.characteristics.training:
        card.append(f'<li><strong>Training:</strong> '
                    f'{animal_data.characteristics.training}</li>')

    if animal_data.characteristics.most_distinctive_feature:
        card.append(f'<li><strong>Distinctive Features:</strong> '
                    f'{animal_data.characteristics.most_distinctive_feature}</li>')

    if animal_data.characteristics.temperament:
        card.append(f'<li><strong>Temperament:</strong> '
                    f'{animal_data.characteristics.temperament}</li>')

    if animal_data.characteristics.name_of_young:
        card.append(f'<li><strong>Offspring Name:</strong> '
                    f'{animal_data.characteristics.name_of_young}</li>')

    if animal_data.characteristics.average_litter_size:
        card.append(f'<li><strong>Average litter size:</strong> '
                    f'{animal_data.characteristics.average_litter_size}</li>')

    if animal_data.characteristics.gestation_period:
        card.append(f'<li><strong>Gestation period:</strong> '
                    f'{animal_data.characteristics.gestation_period}</li>')

    if animal_data.characteristics.incubation_period:
        card.append(f'<li><strong>Incubation period:</strong> '
                    f'{animal_data.characteristics.incubation_period}</li>')

    if animal_data.characteristics.age_of_weaning:
        card.append(f'<li><strong>Age of weaning:</strong> '
                    f'{animal_data.characteristics.age_of_weaning}</li>')

    if animal_data.characteristics.age_of_sexual_maturity:
        card.append(f'<li><strong>Age of sexual maturity:</strong> '
                    f'{animal_data.characteristics.age_of_sexual_maturity}</li>')

    if animal_data.characteristics.age_of_molting:
        card.append(f'<li><strong>Age of molting:</strong> '
                    f'{animal_data.characteristics.age_of_molting}</li>')

    if animal_data.characteristics.weight:
        card.append(f'<li><strong>Weight:</strong> '
                    f'{animal_data.characteristics.weight}</li>')

    if animal_data.characteristics.height:
        card.append(f'<li><strong>Height:</strong> '
                    f'{animal_data.characteristics.height}</li>')

    if animal_data.characteristics.length:
        card.append(f'<li><strong>Length:</strong> '
                    f'{animal_data.characteristics.length}</li>')

    if animal_data.characteristics.wingspan:
        card.append(f'<li><strong>Wingspan:</strong> '
                    f'{animal_data.characteristics.wingspan}</li>')

    if animal_data.characteristics.top_speed:
        card.append(f'<li><strong>Top speed:</strong> '
                    f'{animal_data.characteristics.top_speed}</li>')

    if animal_data.characteristics.lifespan:
        card.append(f'<li><strong>Lifespan:</strong> '
                    f'{animal_data.characteristics.lifespan}</li>')

    if animal_data.characteristics.estimated_population_size:
        card.append(f'<li><strong>Estimated population size:</strong> '
                    f'{animal_data.characteristics.estimated_population_size}</li>')

    if animal_data.characteristics.biggest_threat:
        card.append(f'<li><strong>Biggest threat:</strong> '
                    f'{animal_data.characteristics.biggest_threat}</li>')

    if animal_data.characteristics.slogan:
        card.append(f'<li><strong>Slogan:</strong> '
                    f'{animal_data.characteristics.slogan}</li>')

    card.append("</ul>")
    card.append("</div>")
    card.append("</li>")
    return "\n".join(card) + "\n"


def generate_html_content(animal_name, animal_list):
    html_parts = []

    if not animal_list:
        html_parts.append(f"<h3>Alas, the databank holds no creature by the name '{animal_name}'.<br>"
                f"Let this be the whisper of destiny—a call to wander the wild unknown,<br>"
                f"where hidden marvels await your gentle touch to name them, forever as '{animal_name}'.</h3>")
    else:
        html_parts.append(f"<h2>All Animals matching {animal_name.upper()}:</h2>")
        html_parts.extend(generate_animal_card(a) for a in animal_list)

    return "".join(html_parts)


def insert_data_into_template(template, animals_html):
    """
    Combine template with generated animal HTML.
    :param template: HTML template string
    :param animals_html: Generated animal cards HTML
    :return: Complete HTML page as string
    """
    return template.replace("__REPLACE_ANIMALS_INFO__", animals_html)


def main():
    """
    Main function that orchestrates the program flow:
    1. Get animal from user
    2. Load and process animal data
    5. Generate and save HTML
    """
    animal_name = get_user_animal()
    matching_animals = data_fetcher.fetch_data(animal_name)
    animal_list = data_processing.process_animal_data(matching_animals)

    animals_html = generate_html_content(animal_name, animal_list)
    #Generate HTML
    html_template = load_html_template("animals_template.html")
    final_html = insert_data_into_template(html_template, animals_html)
    save_to_file("animals.html", final_html)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()