



shoppingList = list()



menu = """
    Main Menu
[1] Products
[2] Your shopping list
[Q] For quit

"""


productList = """
    List of Products 
[1] Chocolate      1 bar        0,75$
[2] Tomato         1 kg         3,00$
[3] Milk           1 packet     1,25$
[4] Bread          1 loaf       0,75$
[5] Avocado        1 kg         2,25$
[6] Frozen Potato  1 packet     3,20$

"""


def adding(product:tuple,list:list):
    list.append(product)
    print("Adding is succesful")
    print("Please,press 'enter' for returning to main menu")
    input()


def show(list:list):
    for i in list:
        print("Product: {} amount(s) of {}  ----->>>>> Price: {}*{}  ".format(i[1],i[0],a,i[2]))

    print("Press 'enter' for returning to main menu")
    input()


while True:

    print(menu)
    secim = input("Please,choose your operation:  ")

    if secim == "1":
        print(productList)
        secim2 = input("Please,choose your product:  ")
        a = input("Please,write amount:  ")

        product = tuple()

        if secim2 == "1":
            name = "Chocolate"
            product = (name,a,0.75)
            adding(product,shoppingList)





        elif secim2 == "2":
            name = "Tomato"
            product = (name,a,3.00)
            adding(product,shoppingList)







        elif secim2 == "3":
            name = "Milk"
            product = (name,a,1.25)
            adding(product,shoppingList)









        elif secim2 == "4":
            name = "Bread"
            product = (name,a,0.75)
            adding(product,shoppingList)





        elif secim2 == "5":
            name = "Avocado"
            product = (name,a,2.25)
            adding(product,shoppingList)









        elif secim2 == "6":
            name = "FrozenPotato"
            product = (name,a,3.20)
            adding(product,shoppingList)





        else:
            print("Wrong choice")


    elif secim == "2":
        show(shoppingList)










    elif secim == "Q" or secim == "q":
        print("Hope to see you again!")
        quit()





    else:
        print("Wrong choice")