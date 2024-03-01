class Student:
    ...
    

def main():
        student = get_student()
        print(f"{student.name} from {student.clg}")


def get_student():
        student = Student() 
        student.name = input("Name: ")
        student.clg = input("clg: ")
        return student

if __name__ == "__main__":
    main()
