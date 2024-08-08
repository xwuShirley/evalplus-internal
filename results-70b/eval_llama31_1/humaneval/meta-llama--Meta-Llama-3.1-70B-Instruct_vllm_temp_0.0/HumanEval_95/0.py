def check_dict_case(dict):
    """
    Given a dictionary, return True if all keyspositorhis or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.

    Parameters:
    dict (dict): The input dictionary to be checked.

    Returns:
    bool: True if all keys are strings in either lower case or upper case, else False.
    """

    # Check if the dictionary is empty
    if not dict:
        return False

    # Get the case of the first key
    first_key_case = dict.keys().__iter__().__next__().islower()

    # Check if all keys have the same case as the first key
    for key in dict:
        # If the key is not a string, return False
        if not isinstance(key, str):
            return False
        # If the case of the key does not match the case of the first key, return False
        if key.islower() != first_key_case:
            return False

    # If all keys have the same case, return True
    return True

# Example use cases:
print(check_dict_case({"a":"apple", "b":"banana"}))  # True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))  # False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))  # False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))  # True
print(check_dict_case({}))  # False