class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("missing name")
        self.name = name

# Corrected class name
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

# Corrected class name
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Corrected instantiation of the Professor class
wizard = Wizard("Albus")
student = Student("Harry", "Hyderabad")
professor = Professor("God", "Computer Science")
