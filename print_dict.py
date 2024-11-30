# print_dict.py

# function for printing dictionaries using recursive traversal
def print_dict(data, indent=0):
    """
    recursively print a dictionary in a structured and readable format.
    """
    for key, value in data.items():

        # handle nested dictionaries"
        if isinstance(value, dict):
            print("\n" + f"{key}:" + "\n")
            print_dict(value, indent + 4)

        # handle lists (e.g. cpu usage per core, network interfaces)
        elif isinstance(value, list):
            print("\n" + " " * indent + f"{key}:" + "\n")
            for item in value:

                if isinstance(item, dict):  # if list contains dictionaries
                    print_dict(item, indent + 4)
                else:
                    print(" " * (indent + 4) + f"- {item}")
            print("\n") # should print once list is done

        # handle plain values
        else:
            print(" " * indent + f"{key}: {value}")