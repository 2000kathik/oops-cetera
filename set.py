students = [
    {"name": "karthik", "house": "chaina"}, 
    {"name": "gaga", "house": "canada"}, 
    {"name": "lakshmi", "house": "uae"}, 
    {"name": "ragu", "house": "japan"}, 
    {"name": "mahes", "house": "usa"}
]

houses = set()
for student in students:
    houses.add(student["house"])
        

for house in sorted(houses):
    print(house)