def main():
    student = get_student()
    if student["name"] == "padma":
        student["clg"] == "chirala"
    
    print(f"{student['name']} from {student['clg']}")

def get_student():
   
    name = input("Name: ")
    clg = input("clg: ")
    return {"name": name, "clg": clg}    

if __name__ == "__main__":
    main()