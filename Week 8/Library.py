

class Library:
    def __init__(self, name : str, books : list) -> None:
        self._libraryName = name
        # Library HAS-A book
        self._bookList = books
    
    def __str__(self) -> str:
        outputString = f'{self._libraryName}'
        
        for book in self._bookList:
            outputString += f'\n {book}'
            
        return outputString
    