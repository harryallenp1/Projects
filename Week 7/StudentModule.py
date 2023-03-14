class Student:

    def __init__(self, id : int, name : str) ->None:
        """constuctor to initialise all the instance variables to default 
        Parameters """

        self.__id = id

        self._name = name

    def __str__(self) ->str:

        """This function returns a string containing the values of all class variables

        accepts none and then retuns the string"""
        

        return f'Student ID = {self.__id} {self._name}'