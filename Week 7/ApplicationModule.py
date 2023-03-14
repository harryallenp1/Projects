from StudentModule import Student

class Application:
    def runApp(self):
        self.testStudent()
        
    def testStudent(self):
        stud1 = Student(101,"Alex")
        print(f'stud1 : {stud1}')
        
        stud2 = Student(102,"Bob")
        print(f'stud2 : {stud2}')
        
        stud3 = Student(103,"John")
        print(f'stud3 : {stud3}')
        
        stud1 = Student(101,"Alex")
        print(f'stud1 : {stud1}')
        
        stud4 = Student(104,"Chris")
        print(f'stud4 : {stud4}')
      
app = Application()
app.runApp()


