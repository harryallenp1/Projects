from StudentModule import Student

class Application:
    def runApp(self):
        self.testStudent()

    def testStudent(self):
        stud1 = Student(101, "Alex")
        print(f'stud1 : {stud1}')

        stud2 = Student(102, "Bob")
        print(f'stud2 : {stud2}')

        stud3 = Student(103, "Alex")
        print(f'stud3 : {stud3}')

        #copy one object into another
        #both the objects refer to the same memory location
        stud4 = stud2 
        print(f'stud4 : {stud4}')

        #by default, objects are compared using the memory location
        #; not the values
        if (stud1 == stud2):
            print(f'stud1 and stud2 are SAME')
        else:
            print(f'stud1 and stud2 are DIFFERENT')

        if (stud1 == stud3):
            print(f'stud1 and stud3 are SAME')
        else:
            print(f'stud1 and stud3 are DIFFERENT')

        # stud4.__id = 104 
        # #cannot access private member outside class

        #mutator method - changes the value of instance variable
        stud4.setID(104)

        stud4._name = "Den"
        print(f'stud4 : {stud4}')

        print(f'stud2 ID : {stud2.getID()} stud4 Id : {stud4.getID()}')

        if (stud2 == stud4):
            print(f'stud2 and stud4 are SAME')
        else:
            print(f'stud2 and stud4 are DIFFERENT')

        stud3 = Student(101, "Alex")
        print(f'stud3 : {stud3}')

        if (stud1 == stud3):
            print(f'stud1 and stud3 are SAME')
        else:
            print(f'stud1 and stud3 are DIFFERENT')


app = Application()
app.runApp()