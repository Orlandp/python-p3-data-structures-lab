spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Return a list of names from the spicy_foods list."""
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    """Return a list of foods with heat_level greater than 5."""
    result = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            result.append(food)
    return result

def print_spicy_foods(spicy_foods):
    """Print each food in the format: Name (Cuisine) | Heat Level: 🌶 repeated."""
    chili = "\U0001F336"  # 🌶 emoji
    for food in spicy_foods:
        heat_icons = chili * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_icons}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return the first food dictionary whose cuisine matches, else None."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None



def print_spiciest_foods(spicy_foods):
    """Print only foods with heat_level > 5."""
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    
    """Return the integer average heat level of all foods (0 if empty)."""
    if not spicy_foods:
        return 0
    total = 0
    for food in spicy_foods:
        total += food["heat_level"]
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
     """Add a new spicy_food dictionary to the list and return it."""
     spicy_foods.append(spicy_food)
     return spicy_foods
