import re

def is_valid_email(email):
    """
    Check if the provided email address is valid or not.

    Parameters:
    - email (str): Email address to be validated.

    Returns:
    - bool: True if the email address is valid, False otherwise.

    Example:
    >>> is_valid_email('example@example.com')
    True
    >>> is_valid_email('invalid_email')
    False
    """

    # Regular expression pattern for validating email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

def is_valid_password(password):
    """
    Check if the provided password meets the criteria:
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special symbol

    Parameters:
    - password (str): Password to be validated.

    Returns:
    - tuple: A tuple containing a boolean indicating if the password is valid and a message.

    Example:
    >>> is_valid_password('Abcdef1!')
    (True, 'Password is valid')
    >>> is_valid_password('password')
    (False, 'Password must contain at least one digit')
    """

    # Regular expression pattern for validating password
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[A-Za-z\d!@#$%^&*()_+]+$'

    # Check if the password matches the pattern
    if re.match(password_pattern, password):
        return True, 'Password is valid'
    else:
        message = "Password must contain "
        if not re.search(r'[a-z]', password):
            message += "at least one lowercase letter"
        if not re.search(r'[A-Z]', password):
            if "lowercase letter" in message:
                message += ", "
            message += "at least one uppercase letter"
        if not re.search(r'\d', password):
            if "uppercase letter" in message or "lowercase letter" in message:
                message += ", "
            message += "at least one digit"
        if not re.search(r'[!@#$%^&*()_+]', password):
            if "uppercase letter" in message or "lowercase letter" in message or "digit" in message:
                message += ", "
            message += "at least one special symbol"

        return False, message


