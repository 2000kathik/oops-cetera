#return with constructor:
class Student:
    def __init__(self, name, clg):
        self.name = name
        self.clg = clg  

def main():
        student = get_student()
        print(f"{student.name} is from {student.clg}")

def get_student():
        
    name = input("name: ")
    clg = input("clg: ")
    return Student(name, clg)       
     
if __name__ == "__main__":
    main()
