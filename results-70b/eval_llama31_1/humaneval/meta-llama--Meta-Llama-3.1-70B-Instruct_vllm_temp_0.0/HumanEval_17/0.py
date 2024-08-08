from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    This function takes a string representing musical notes in a special ASCII format, 
    parses this string and returns a list of integers corresponding to how many beats does each note last.

    :param music_string: A string representing musical notes in a special ASCII format
    :return: A list of integers corresponding to how many beats does each note last
    """

    # First, we split the input string into a list of notes
    notes = music_string.split()

    # Then, we initialize an empty list to store the duration of each note
    durations = []

    # We iterate over each note in the list of notes
    for note in notes:
        # For each note, we check its type and append the corresponding duration to the durations list
        if note == 'o':
            durations.append(4)  # whole note lasts four beats
        elif note == 'o|':
            durations.append(2)  # half note lasts two beats
        elif note == '.|':
            durations.append(1)  # quater note lasts one beat

    # Finally, we return the list of durations
    return durations