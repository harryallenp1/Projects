from ItemModule import Item

class Application:
    def __init__(self):
        self.item = Item()

    def run(self):
        while True:
            print(f'{"-"*105}')
            print(f'{"-"*105}')

            print("\nPlease select an option:")
            print("1. Add Item")
            print("2. Edit Item")
            print("3. Delete Item")
            print("4. Search Item")
            print("5. Display Item List")
            print("6. Exit")
            
            
            print(f'{"-"*105}')
            print(f'{"-"*105}')

            try:
                choice = int(input())
            except ValueError:
                print("Invalid input! Please enter a number from 1 to 6.")
                continue

            if choice == 1:
                self.item.Add()
            elif choice == 2:
                self.item.Edit()
            elif choice == 3:
                self.item.Delete()
            elif choice == 4:
                self.item.Search()
            elif choice == 5:
                self.item.Display()
            elif choice == 6:
                print("Exiting the program...")
                break
            else:
                print("Invalid input! Please enter a number from 1 to 6.")
                continue


app = Application()
app.run()