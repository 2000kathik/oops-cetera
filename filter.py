#filter:
students = [
    {"name": "hermione", "house": "gryffindor"}, 
    {"name": "harry", "house": "gryffindor"}, 
    {"name": "ron", "house": "gryffindor"}, 
    {"name": "draco", "house": "slytherin"},
]

def is_gryffindor(s):
    return s["house"] == "gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])