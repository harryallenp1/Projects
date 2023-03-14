class Book:
    def __init__(self, title: str, author : str , genre : str ) -> None:
        self._title = title 
        self._author = author
        self._genre = genre 
        
    #accessor method 
    def getTitle(self) -> str:
        return self._title
    
    #mutator method 
    def setTitle(self, titl)