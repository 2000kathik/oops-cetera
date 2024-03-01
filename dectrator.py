class Student:

    def __init__(self, name, clg):


        self.name = name
        self.clg = clg

    def __str__(self):
        return f"{self.name} is from {self.clg}" 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    @property
    def clg(self):
        return self._clg
    
    @clg.setter
    def clg(self, clg):
        if clg not in ["au", "svu", "anu", "ou"]:
            raise ValueError("Invalid clg")
        self._clg = clg
            
def main():
        student = get_student()
        student._clg = "Number four, private Drive "
        print(student)

def get_student():
        
    name = input("name: ")
    clg = input("clg: ")
    
    return Student(name, clg)       
     
if __name__ == "__main__":
    main()