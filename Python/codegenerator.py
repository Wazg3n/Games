def code_generator(length):
    """Generates a random alphanumeric code of the specified length."""
    import random
    import string
    
    # Generate a random string of alphanumeric characters
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    
    return code

# Example usage
print(code_generator(8))  # Outputs a random 8-character code
print(code_generator(12))  # Outputs a random 12-character code
