class Student:
    def __init__(self, name, cls, patronus):
        if not name:
            raise ValueError("missing name")
        if cls not in ["au", "svu", "anu", "ou"]:
            raise ValueError("Invalid cls")
        self.name = name
        self.cls = cls
        self.patronus = patronus
    def __str__(self):
        return f"{self.name} from {self.cls}" 
    
    def charm(self):
        match self.patronus:
            case "stag":
                return " # "
            case "otter":
                return "*"
            case "jack russel":
                return "/"
            case _:
                return "-"


            
def main():
        student = get_student()
        print("expecto patrinus!")
        print(student.charm())

def get_student():
        
    name = input("name: ")
    cls = input("cls: ")
    patronus = input("patronus: ")
    return Student(name, cls, patronus)      
     
if __name__ == "__main__":
    main()