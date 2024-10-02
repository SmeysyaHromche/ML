import json
import jsonschema
from typing import Dict
def parse_config(config_file_path:str, valid_schema:Dict)->Dict:
    with open(config_file_path, 'r') as file:
        try:
            config_schema = json.load(file)
            jsonschema.validate(config_schema, valid_schema)
            return config_schema
        except FileNotFoundError:
            print("Error! Configuration file is not exist.")
            exit(1),
        except jsonschema.exceptions.ValidationError as err:
            print(f"Error! Invalid format of configuration file: {err}")
            exit(1)
