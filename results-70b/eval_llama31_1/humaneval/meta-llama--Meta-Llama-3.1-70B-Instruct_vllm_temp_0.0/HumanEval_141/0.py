def file_name_check(file_name):
    """
    Checks if a file name is valid.

    A file name is considered valid if:
    - It contains no more than three digits.
    - It contains exactly one dot.
    - The substring before the dot is not empty and starts with a latin alphabet letter.
    - The substring after the dot is one of 'txt', 'exe', or 'dll'.

    Args:
        file_name (str): The name of the file to check.

    Returns:
        str: 'Yes' if the file name is valid, 'No' otherwise.
    """
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into two parts: before and after the dot
    before_dot, after_dot = file_name.split('.')

    # Check if the substring before the dot is not empty and starts with a latin alphabet letter
    if not before_dot or not before_dot[0].isalpha():
        return 'No'

    # Check if the substring after the dot is one of 'txt', 'exe', or 'dll'
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    # Check if the file name contains no more than three digits
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'

    return 'Yes'