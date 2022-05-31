

a = 'abcdef'
i = 0

tester = {}
aux = {}
while i < len(a):
    tester[a[i]] = i
    
    i+=1

tester['a'] = tester.get('a', 0) + 5
print(tester)
        
        
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        #Person.__init__(self, fname, lname)
        super().__init__(fname, lname) 
        print("hmm")

p1 = Student("James", "Brown")
p1.printname()
