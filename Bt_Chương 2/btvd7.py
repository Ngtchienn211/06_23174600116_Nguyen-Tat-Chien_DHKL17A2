import json

json_data = '''
{
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "skills": ["Python", "JavaScript", "Machine Learning"]
}
'''

python_obj = json.loads(json_data)

print(python_obj)
print(type(python_obj))

print("Name:", python_obj["name"])
print("Age:", python_obj["age"])
print("City:", python_obj["city"])
print("Skills:", python_obj["skills"])
