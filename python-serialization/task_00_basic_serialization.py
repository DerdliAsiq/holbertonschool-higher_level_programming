<<<<<<< HEAD
=======
#!/usr/bin/env python3
"""Basic serialization module."""
>>>>>>> 7158139 (added new repo)
import json


def serialize_and_save_to_file(data, filename):
<<<<<<< HEAD
    """
    Takes a Python dictionary (data) and saves it to a file in JSON format.
    Cybersec Context: Like malware saving stolen credentials to a local file
    before exfiltrating them.
    """
    # 'w' mode means write. It will create the file or overwrite it.
    with open(filename, 'w') as f:
        # json.dump takes the object and the file handler
=======
    """Serialize and save data to file."""
    with open(filename, 'w', encoding='utf-8') as f:
>>>>>>> 7158139 (added new repo)
        json.dump(data, f)


def load_and_deserialize(filename):
<<<<<<< HEAD
    """
    Reads a JSON file and turns it back into a Python dictionary.
    Cybersec Context: Like a security tool reading a config file to set up
    firewall rules.
    """
    # 'r' mode means read.
    with open(filename, 'r') as f:
        # json.load reads the file and returns the Python object
=======
    """Load and deserialize data from file."""
    with open(filename, 'r', encoding='utf-8') as f:
>>>>>>> 7158139 (added new repo)
        return json.load(f)
