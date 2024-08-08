from datetime import datetime

def valid_date(date):
    """
    This function validates a given date string and returns True if the date is valid otherwise False.
    
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. 
    And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. 
    And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy
    
    Parameters:
    date (str): The date string to be validated.
    
    Returns:
    bool: True if the date is valid, False otherwise.
    """

    # Check if the date string is empty
    if not date:
        return False

    # Check if the date string is in the correct format
    try:
        datetime.strptime(date, '%m-%d-%Y')
    except ValueError:
        return False

    # Split the date string into month, day, and year
    month, day, year = date.split('-')

    # Check if the month is valid
    if not 1 <= int(month) <= 12:
        return False

    # Check if the day is valid
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if not 1 <= int(day) <= 31:
            return False
    elif month in ['04', '06', '09', '11']:
        if not 1 <= int(day) <= 30:
            return False
    else:
        if not 1 <= int(day) <= 29:
            return False

    # If all checks pass, the date is valid
    return True