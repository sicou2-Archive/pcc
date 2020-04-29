"""A module for returning a 'City, Country' string."""

def a_city(city, country, population=None):
    """Generate a neatly formatted 'City, Country'"""
    if population:
        city_country = f"{city}, {country}, population: {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()