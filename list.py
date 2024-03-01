students = [
    {"name": "karthik", "house": "ts"}, 
    {"name": "gaga", "house": "AP"}, 
    {"name": "lakshmi", "house": "mp"}, 
    {"name": "ragu", "house": "mum"}, 
    {"name": "mahes", "house": "usa"}
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
