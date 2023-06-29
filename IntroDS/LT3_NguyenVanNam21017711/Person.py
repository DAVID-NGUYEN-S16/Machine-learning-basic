class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def setName(self, name):
        self.__name = name
    def setAddress(self, address):
        self.__address = address
    
    def __str__(self):
        return f'Name: {self.__name} \nAddress: {self.__address}'
class Student(Person):
    def __init__(self,__name, __address, scoreMath, scorePhysical, scoreChemistry):
        super().__init__(__name, __address)
        self.__scoreMath = scoreMath
        self.__scorePhysical = scorePhysical
        self.__scoreChemistry = scoreChemistry
    def getscoreMath(self):
        return self.__scoreMath
    def getscorePhysical(self):
        return self.__scorePhysical
    def getscoreChemistry(self):
        return self.__scoreChemistry
    def setscoreMath(self, scoreMath):
        self.__scoreMath = scoreMath
    def setscorePhysical(self, scorePhysical):
        self.__scorePhysical = scorePhysical
    def setscoreChemistry(self, scoreChemistry):
        self.__scoreChemistry = scoreChemistry
    def __str__(self):
        return f'Name: {self.getName()} \nAddress: {self.getAddress()} \nscoreMath: {self.__scoreMath} \nscorePhysical: {self.__scorePhysical} \nscoreChemistry: {self.__scoreChemistry}'
class Teacher(Person):
    def __init__(self, name, address, subject):
        super().__init__(name, address)
        self.__subject = subject
    def getsubject(self):
        return self.__subject
    def setself(self, subject):
        self.__subject = subject
    def __str__(self):
        return f'Name: {self.getName()} \nAddress: {self.getAddress()} \n subject: {self.__subject}'
## Test class Person
person1 = Person("John", "Go Vap")
print(person1.__str__())
## Test class Student

student1 = Student("Alis", "Go Vap", 5, 6, 7)
print(student1.__str__())

## Test class Teacher
teacher1 = Teacher("Luis", "Binh Tan", 'Van')
print(student1.__str__())