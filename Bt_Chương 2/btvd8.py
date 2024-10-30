import json

python_obj = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "Machine Learning"]
}

json_data = json.dumps(python_obj)

print("JSON String:", json_data)

for key, value in python_obj.items():
    print(f"{key}: {value}")
