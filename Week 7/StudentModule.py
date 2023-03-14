class Student:
    def __init__(self, id : int, name : str) -> None:
        """
        constructor to initialize all the instance variables to default value
        Parameters: 2 parameters, id = Int, name = string
        returns: an object of the Student class
        """
        # private variables using __ (double undescore)
        # only accessible within class and its method
        self.__id = id
        self._name = name #non-private member

    #document string or docstring
    #used to describe a function in documentation
    def __str__(self) -> str:
        """ This function will return a string 
        containing the values of all class variable.
        accepts no parameter
        returns string"""

        return f'Student ID = {self.__id}, Name = {self._name}'
    
    #operator overloading
    def __eq__(self, anotherObj : object) -> bool:
        """
        This function will compare two objects of the Student class
        to match the __id variable
        returns true if the __id of both the objects are matching
        otherwise, returns false

        Overloading the == (equality) operator
        replace the default behaviour of compare by memory to compare by values
        """

        if (self.__id == anotherObj.__id):
        # if (self.__id == anotherObj.__id) and (self._name == anotherObj.__name):
            return True
        else:
            return False
    

    #mutator method - changes the value of instance variable
    #setter
    def setID(self, id : int):
        self.__id = id

    #accessor method - returns the value of instance variable
    #getter
    def getID(self) -> int:
        return self.__id