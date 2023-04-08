class Item:
    FILENAME = 'CollectibleDB.txt'
    FILE = None

    def __init__(self):
        try:
            self.FILE = open(self.FILENAME, 'a')
        except IOError:
            print(f'Error: Unable to open file {self.FILENAME}')

    @staticmethod
    def Add():
        try:
            with open(Item.FILENAME, 'r') as f:
                last_id = 0
                for line in f:
                    fields = line.strip().split(',')
                    last_id = max(last_id, int(fields[0]))
        except FileNotFoundError:
            last_id = 0

        id = str(last_id + 1)
        title = input('Enter Title: ')
        author = input('Enter Author: ')
        genre = input('Enter Genre: ')
        publisher = input('Enter Publisher: ')

        record = f'{id},{title},{author},{genre},{publisher}\n'
        try:
            with open(Item.FILENAME, 'a') as f:
                f.write(record)
            print('Item added successfully.')
        except Exception as e:
            print(f'Error: {e}')

        @staticmethod
        def Edit():
            id = input('Enter ID to edit: ')
            records = []
            found = False
            try:
                with open(Item.FILENAME, 'r') as f:
                    for line in f:
                        if line.startswith(id):
                            found = True
                            print('Enter new details:')
                            title = input('Enter Title: ')
                            author = input('Enter Author: ')
                            genre = input('Enter Genre: ')
                            publisher = input('Enter Publisher: ')
                            record = f'{id},{title},{author},{genre},{publisher}\n'
                            records.append(record)
                        else:
                            records.append(line)
                if found:
                    try:
                        with open(Item.FILENAME, 'w') as f:
                            f.writelines(records)
                        print('Item updated successfully.')
                    except Exception as e:
                        print(f'Error: {e}')
                else:
                    print(f'Error: Item with ID {id} not found.')
            except IOError:
                print(f'Error: Unable to open file {Item.FILENAME}')

    @staticmethod
    def Delete():
        id = input('Enter ID to delete: ')
        records = []
        found = False
        try:
            with open(Item.FILENAME, 'r') as f:
                for line in f:
                    if line.startswith(id):
                        found = True
                    else:
                        records.append(line)
            if found:
                try:
                    with open(Item.FILENAME, 'w') as f:
                        f.writelines(records)
                    print('Item deleted successfully.')
                except Exception as e:
                    print(f'Error: {e}')
            else:
                print(f'Error: Item with ID {id} not found.')
        except IOError:
            print(f'Error: Unable to open file {Item.FILENAME}')

    @staticmethod
    def Search():
        name = input('Enter item name to search: ')
        found = False
        try:
            with open(Item.FILENAME, 'r') as f:
                for line in f:
                    if name.lower() in line.lower():
                        id, title, author, genre, publisher = line.strip().split(',')
                        print(
                            f'ID: {id}\nTitle: {title}\nAuthor: {author}\nGenre: {genre}\nPublisher: {publisher}\n')
                        found = True
            if not found:
                print(f'Error: Item with name {name} not found.')
        except IOError:
            print(f'Error: Unable to open file {Item.FILENAME}')

    @staticmethod
    def Display():
        try:
            with open(Item.FILENAME, 'r') as file:
                print("{:<5} {:<20} {:<20} {:<15} {:<20}".format(
                    "ID", "Title", "Author", "Genre", "Publisher"))
                print("{:<5} {:<20} {:<20} {:<15} {:<20}".format(
                    "-" * 5, "-" * 20, "-" * 20, "-" * 15, "-" * 20))
                for line in file:
                    data = line.strip().split(",")
                    print("{:<5} {:<20} {:<20} {:<15} {:<20}".format(
                        data[0], data[1], data[2], data[3], data[4]))
                print()
        except FileNotFoundError:
            print("CollectibleDB.txt file not found!")