from ProductModule import Product

class Application:
    def __init__(self):
        self.productList = [] #empty list

    def addProduct(self):
        print("Trying to add product")
        print()

        #ask user for product details
        ID = int(input("Enter product ID : "))
        prodName = input("Enter product name : ")
        prodPrice = float(input("Enter product price : "))

        #create product object using user input
        # newProduct = Product() #calls the __init__(self)
        # newProduct.id = ID
        # newProduct.pName = prodName
        # newProduct.price = prodPrice

        #call __init__(self, pid: int, pname : str, pprice : float):
        newProduct = Product(ID, prodName, prodPrice)

        #add the product object into list
        self.productList.append(newProduct)

    def editProduct(self):
        print("Trying to edit product")

        if (len(self.productList) == 0):
            print("No product to edit")
        else:
            idToSearch = int(input("Enter the product ID to edit : "))

            for prod in self.productList:
                if (prod.id == idToSearch):
                    print(f'Matching product found \n {prod}')

                    #ask the user for updated details
                    prodName = input("Enter updated product name : ")
                    prodPrice = float(input("Enter updated product price : "))

                    #update the object with updated values
                    prod.pName = prodName
                    prod.price = prodPrice

                    #display updated information
                    # \n - new line
                    print(f'product information modified \n {prod}')

                    break
            else:
                print(f'no matching product with ID : {idToSearch}')

    def deleteProduct(self):
        print("Trying to delete product")

        if (len(self.productList) == 0):
            print("No product to edit")
        else:
            idToSearch = int(input("Enter the product ID to delete : "))

            for prod in self.productList:
                if (prod.id == idToSearch):
                    print(f'Matching product found \n {prod}')

                    #delete the matching object from list
                    self.productList.remove(prod)

                    print(f'product {idToSearch} deleted from list')

                    break
            else:
                print(f'no matching product with ID : {idToSearch}')

    def searchProduct(self):
        print("Trying to search for a product")

        if (len(self.productList) == 0):
            print("No product to search")
        else:
            idToSearch = int(input("Enter the product ID to search : "))

            #for...else
            for prod in self.productList:
                if (prod.id == idToSearch):
                    #matching product found
                    print(f'Matching product found \n {prod}')
                    break
            else:
                #no matching product found 
                # only if for loop ends processing entire list of product
                # if for loop doesn't break

                # for the for..else statement,
                #if there is no break statement in the for loop,
                #then the else will always be executed 
                print(f'No matching product for ID : {idToSearch}')

            print("Searching entire list is completed")

    def displayProductList(self):
        print("Displaying product list")

        if (len(self.productList) == 0):
            print("No products in the list yet")
        else:
            #there are products in the list
            for prod in self.productList:
                # prod - object of Product class
                print(prod) #call __str__() method from class
                # prod.displayProductInfo()

    def runApp(self):
        # display a menu to user for selecting operation
        choice = 0 

        while choice != 6:
            print()
            print("-"*40)
            print(" 1 : Add Product")
            print(" 2 : Edit Product")
            print(" 3 : Search Product")
            print(" 4 : Delete Product")
            print(" 5 : Display Product List")
            print(" 6 : Exit")
            print("-"*40)
            choice = int(input("Please enter your choice : "))
            print("-"*40)
            print()

            if choice == 1:
                self.addProduct()
            elif choice == 2:
                self.editProduct()
            elif choice == 3:
                self.searchProduct()
            elif choice == 4:
                self.deleteProduct()
            elif choice == 5:
                self.displayProductList()
            elif choice == 6:
                print("Terminating the program")
            else:
                print("Invalid Choice")

        #after while loop
        print("continuing after while loop")



    # def runApp(self):
    #     print('Application for maintaining list of products')

    #     #create an object of the Product class
    #     prod1 = Product()
    #     prod1.displayProductInfo()

    #     print("Product2 Info ----------------------------")
    #     prod2 = Product()
    #     prod2.displayProductInfo()

    #     print("Product2 Info Modified ----------------------------")
    #     prod2.id = 101
    #     prod2.pName = "Water Bottle"
    #     prod2.price = 1.99
    #     prod2.displayProductInfo()

    #     print("Product3 Info ----------------------------")
    #     prod3 = Product()
    #     prod3.id = 102
    #     prod3.pName = "Coffee Beans"
    #     prod3.price = 7.99
    #     prod3.displayProductInfo()


#Application class ends

#create object/instance of the Application class
app = Application()

#execute the runApp() 
#access any member of the class using dot operator with object
app.runApp()