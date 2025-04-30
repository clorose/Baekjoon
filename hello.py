def hello(name):
    """
    Function to greet a person with their name.
    
    Args:
        name (str): The name of the person to greet.
        
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Example usage
    name = "Alice"
    print(hello(name))