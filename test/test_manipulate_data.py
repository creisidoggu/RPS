import json

from src.RPS_dict import load_save_data, write_save_data

TEST_JSON_PATH = 'test_manipulate_data.json'

def test_load_save_data_file_not_found():
    result = load_save_data(TEST_JSON_PATH)
    assert result == {}
    
def test_load_save_data_invalid_json():
    with open(TEST_JSON_PATH, "w") as file:
        file.write('{ idk an invalid json bro }')
    result = load_save_data(TEST_JSON_PATH)
    assert result == {}
    
def test_load_save_data_valid_json():
    data = {"key" : "value"}
    with open(TEST_JSON_PATH, "w") as file:
        json.dump(data, file)
    
    result = load_save_data(TEST_JSON_PATH)
    assert result == data
    
def test_write_save_data():
    data = {"key" : "value"}
    write_save_data(TEST_JSON_PATH, data)
    
    with open(TEST_JSON_PATH, "r") as file:
        result = json.load(file)
        
    assert result == data
    
def test_load_and_write_integration():
    data = {"key" : "value"}
    write_save_data(TEST_JSON_PATH, data)
    result = load_save_data(TEST_JSON_PATH)
    assert result == data