import random
import string

def generate_new_otp(length):
    """
    Generate a random OTP (One Time Password) with the specified length.

    Parameters:
    - length (int): Length of the OTP to be generated.

    Returns:
    - str: Generated OTP consisting of digits.

    Example:
    >>> generate_otp(6)
    '583921'
    >>> generate_otp(4)
    '9348'
    """

    otp = ''.join(random.choices(string.digits, k=length))
    return otp


