class Student:
    def __init__(self, name, clg):
        if not name:
            raise ValueError("missing name")
        if clg not in ["anu", "au", "svu", "ou"]:
            raise ValueError("Invalid house")
        self.name = name
        self.clg = clg 
    def __str__(self):
        return f"{self.name} from {self.clg}" 

def main():
        student = get_student()
        print(student)

def get_student():
        
    name = input("name: ")
    clg = input("clg: ")
    return Student(name, clg)      
     
if __name__ == "__main__":
    main()