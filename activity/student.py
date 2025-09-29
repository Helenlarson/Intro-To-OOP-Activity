# add your Student class here!
class Student:
    def __init__(self, name, year, classes):
        self.name = name 
        self.year = year 
        self.classes = classes

    def add_classes(self, subject):
        self.classes.append(subject)
        return self.classes
    
    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        return f"{self.name} is a {self.year} enrolled in {self.get_num_classes()} classes"
