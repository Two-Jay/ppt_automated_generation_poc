import json
import configparser

def read_file(file_path, encoding="utf-8", mode="r", errors="ignore"):
    with open(file_path, mode, encoding=encoding, errors=errors) as file:
        return file.read()

def write_file(file_path, data, encoding="utf-8", mode="w", errors="ignore"):
    with open(file_path, mode, encoding=encoding, errors=errors) as file:
        file.write(data)

def write_json(file_path, data, encoding="utf-8", mode="w", errors="ignore"):
    with open(file_path, mode, encoding=encoding, errors=errors) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_json(file_path, encoding="utf-8", mode="r", errors="ignore"):
    with open(file_path, mode, encoding=encoding, errors=errors) as file:
        return json.load(file)
    
def read_ini(file_path, encoding="utf-8", mode="r", errors="ignore"):
    with open(file_path, mode, encoding=encoding, errors=errors) as file:
        return configparser.ConfigParser(file)
