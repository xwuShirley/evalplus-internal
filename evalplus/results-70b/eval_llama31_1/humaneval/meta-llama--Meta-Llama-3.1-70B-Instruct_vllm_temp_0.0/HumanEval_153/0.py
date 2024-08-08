def Strongest_Extension(class_name, extensions):
    """
    Returns the strongest extension for a given class.

    The strength of an extension is determined by the difference between the number
    of uppercase letters (CAP) and lowercase letters (SM) in its name.

    If multiple extensions have the same strength, the first one in the list is chosen.

    Parameters:
    class_name (str): The name of the class.
    extensions (list): A list of extension names.

    Returns:
    str: A string in the format "ClassName.StrongestExtensionName".
    """

    def calculate_strength(extension):
        """
        Calculates the strength of an extension.

        Parameters:
        extension (str): The name of the extension.

        Returns:
        int: The strength of the extension.
        """
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        return cap - sm

    strongest_extension = max(extensions, key=calculate_strength)
    return f"{class_name}.{strongest_extension}"