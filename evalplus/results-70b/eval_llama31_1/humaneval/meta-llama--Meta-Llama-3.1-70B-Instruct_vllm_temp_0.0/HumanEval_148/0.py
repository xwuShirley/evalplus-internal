def bf(planet1, planet2):
    """
    Returns a tuple of planets whose orbits are between the orbits of planet1 and planet2.
    
    Parameters:
    planet1 (str): Name of the first planet
    planet2 (str): Name of the second planet
    
    Returns:
    tuple: A tuple of planet names in order of their proximity to the Sun
    """
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Check if both planet names are correct
    if planet1 not in planets or planet2 not in planets:
        return ()

    # Find the indices of the two planets
    i = planets.index(planet1)
    j = planets.index(planet2)
    
    # Swap indices if planet1 is after planet2
    if i > j:
        i, j = j, i
    
    # Return the planets in between, excluding the input planets
    return tuple(planets[i+1:j])