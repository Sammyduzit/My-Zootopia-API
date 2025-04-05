from dataclasses import dataclass, field

@dataclass
class Taxonomy:
    kingdom: str = None
    phylum: str = None
    class_name: str = None  # 'class' is a reserved keyword in Python.
    order: str = None
    family: str = None
    genus: str = None
    scientific_name: str = None


@dataclass
class Characteristics:
    most_distinctive_feature: str = None
    temperament: str = None
    training: str = None
    diet: str = None
    average_litter_size: str = None
    type: str = None
    common_name: str = None
    slogan: str = None
    group: str = None
    color: str = None
    skin_type: str = None
    lifespan: str = None
    prey: str = None
    name_of_young: str = None
    habitat: str = None
    predators: str = None
    lifestyle: str = None
    favorite_food: str = None
    top_speed: str = None
    weight: str = None
    height: str = None
    group_behavior: str = None
    estimated_population_size: str = None
    biggest_threat: str = None
    gestation_period: str = None
    number_of_species: str = None
    age_of_sexual_maturity: str = None
    age_of_weaning: str = None


@dataclass
class Animal:
    """Complete animal data structure with taxonomy and characteristics."""
    name: str = None
    taxonomy: Taxonomy = field(default_factory=Taxonomy)
    locations: list = field(default_factory=list)
    characteristics: Characteristics = field(default_factory=Characteristics)


def create_animal_instance(animal_data):
    """
    Create an Animal instance from raw JSON data.
    :param animal_data: Dictionary containing animal data
    :return: Structured Animal object with all data
    """
    taxonomy_data = animal_data.get("taxonomy", {})
    characteristics_data = animal_data.get("characteristics", {})

    taxonomy = Taxonomy(
        kingdom=taxonomy_data.get("kingdom"),
        phylum=taxonomy_data.get("phylum"),
        class_name=taxonomy_data.get("class"),
        order=taxonomy_data.get("order"),
        family=taxonomy_data.get("family"),
        genus=taxonomy_data.get("genus"),
        scientific_name=taxonomy_data.get("scientific_name"),
    )

    characteristics = Characteristics(
        most_distinctive_feature=characteristics_data.get("most_distinctive_feature"),
        temperament=characteristics_data.get("temperament"),
        training=characteristics_data.get("training"),
        diet=characteristics_data.get("diet"),
        average_litter_size=characteristics_data.get("average_litter_size"),
        type=characteristics_data.get("type"),
        common_name=characteristics_data.get("common_name"),
        slogan=characteristics_data.get("slogan"),
        group=characteristics_data.get("group"),
        color=characteristics_data.get("color"),
        skin_type=characteristics_data.get("skin_type"),
        lifespan=characteristics_data.get("lifespan"),
        prey=characteristics_data.get("prey"),
        name_of_young=characteristics_data.get("name_of_young"),
        habitat=characteristics_data.get("habitat"),
        predators=characteristics_data.get("predators"),
        lifestyle=characteristics_data.get("lifestyle"),
        favorite_food=characteristics_data.get("favorite_food"),
        top_speed=characteristics_data.get("top_speed"),
        weight=characteristics_data.get("weight"),
        height=characteristics_data.get("height"),
        group_behavior=characteristics_data.get("group_behavior"),
        estimated_population_size=characteristics_data.get("estimated_population_size"),
        biggest_threat=characteristics_data.get("biggest_threat"),
        gestation_period=characteristics_data.get("gestation_period"),
        number_of_species=characteristics_data.get("number_of_species"),
        age_of_sexual_maturity=characteristics_data.get("age_of_sexual_maturity"),
        age_of_weaning=characteristics_data.get("age_of_weaning")
    )

    return Animal(
        name=animal_data.get("name"),
        taxonomy=taxonomy,
        locations=animal_data.get("locations", []),
        characteristics=characteristics,
    )


def process_animal_data(animals_json_data):
    """
    Convert raw animal data into structured Animal objects.
    :param animals_json_data: List of animal dictionaries from JSON
    :return:
    """
    animals = []
    for animal_data in animals_json_data:
        try:
            animal = create_animal_instance(animal_data)
            animals.append(animal)
        except Exception as e:
            print(f"Error parsing animal data: {e}")

    return animals
