import json

python_dict = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "Machine Learning"]
}

json_data = json.dumps(python_dict, sort_keys=True, indent=4)

print(json_data)
