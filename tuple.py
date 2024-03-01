def main():
    student = get_student()
    if student[0] == "karthik":
        student[1] == "bapatla"
    print(f"{student[0]} is from {student[1]}")

def get_student():
    name = input("Name: ")
    clg = input("clg: ")
    return [name, clg]    

if __name__ == "__main__":
    main()
