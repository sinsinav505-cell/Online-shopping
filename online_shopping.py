items_dict={"fruits":{"orange":30},
            "vegetables":{"carrot":20},"dress":{"shirt":800},
            "electronics":{"Fridge":800000}}

cart={}

class shopping:

    def add_items(self):
        category = input("Enter the category:")
        number = int(input("Enter no of items to be added:"))

        if category not in items_dict:
            items_dict[category]={}

        for i in range(number):
            item=input("Enter item:")
            price=int(input("Enter price:"))
            items_dict[category][item]=price
            print("Added")


    def show_categories(self): #show all category name
        print("Categories:\n")
        for name in items_dict:
            print(f"Category:{name}")

    def show_category_items(self,category): #show choosen category's item and price
        if category in items_dict:
            print(f"\n-----{category.upper()}-----")
            for item,price in items_dict[category].items():
                print(f"{item} : {price}")

    def remove_category(self,category): # removes choosen category
        if category in items_dict:
            print(f"Are you sure ? Do you want to delete {category} category ?") 
            r_op=int(input("\n 1.yes \n 2.no \n enter 1 or 2: "))
            if r_op==1:
                del items_dict[category]
                print("Category Deleted")

            elif r_op==2:
                print("Not Deleted ")

            else:
                print("Invalid option")


    def remove_item(self,item,category):
        if item in items_dict[category]:
            print(f"Are you sure ? Do you want to delete {item} item ?") 
            i_op=int(input("\n 1.yes \n 2.no \n enter 1 or 2: "))

            if i_op==1:
                del items_dict[category][item]
                print("Item Deleted")

            elif i_op==2:
                print("Not Deleted ")

            else:
                print("Invalid option")

    def add_cart(self,item,category):
        if category in items_dict and item in items_dict[category]:
            a_op=int(input("\n Do you want to add this item to cart? \n 1.Yes \n 2.No \n Enter 1 or 2:"))

            if a_op==1:
                price = items_dict[category][item]
                if item in cart:
                    cart[item]["quantity"]+= 1
                else:
                    cart[item] = {"price": price, "quantity": 1}
                    print(f"{item} Added to cart.")
                    print(f"Item Name:{item},Price:{cart[item]["price"]},Quantity:{cart[item]["quantity"]}")



    def remove_from_cart(self,item):
        if item in cart:
            r_cart=int(input("\n Do you want to remove the item from cart: \n 1.Yes \n 2.No \n Enter 1 or 2:"))
            if r_cart==1:
                del cart[item]
                print("Removed from cart")
            elif r_cart==2:
                print("Not Removed")
            else:
                print("Invalid option")



    def view_cart(self):
        if not cart: #if cart is empty 
            print("Cart is empty")
        else:
            print("Items in cart are:")
            for name,value in cart.items():
                print(f"Item Name:{name} , Price:{value['price']} , Quantity:{value['quantity']}")


    def buy_and_checkout(self):
        if not cart:   
            print("Cart is empty")
            return

        buy = int(input("Do you want to buy the products in the cart:"
                        " \n 1.Yes \n 2.No \n Enter 1 or 2 : "))

        if buy == 1:
            print("\n ----- Checkout ----- ")
            total = 0

            for name, value in cart.items():
                item_total = value["price"] * value["quantity"]
                total += item_total
                print(f"{name} ({value['quantity']} x {value['price']}) = {item_total}")

            print(f"\n Total Amount = {total}")

            clear_cart = int(input("\nDo you want to clear the cart after checkout?"
                                " \n 1.Yes \n 2.No \n Enter 1 or 2: "))

            if clear_cart == 1:
                cart.clear()
                print("Cart cleared. Thank you for shopping!")
            else:
                print("Cart not cleared. You can continue shopping.")

        elif buy == 2:
            print("Checkout cancelled.")
        else:
            print("Invalid option")
                      


obj=shopping()


def show_items():
    for name,value in items_dict.items(): #name is the category and value is items dictionary {category:{items:price}}   -  {name:{value:price}}
        print(f"Category:{name}")
        for item,price in value.items(): #here value is the items dictionary which consist item name and price
            print(f"{item}:{price}")



def options():
    while True:
        op=int(input("Hi \n Select a option: " 
        " \n  1.Add product " 
        " \n  2.Show Categories   " 
        " \n  3.Remove Category"
        " \n  4.Remove item from Category "
        " \n  5.Add to cart"
        " \n  6.Remove from cart"
        " \n  7.View cart"
        " \n  8.Buy and checkout"
        " \n  9.Exit" 
        " \n Enter option:"))
        if op==1: #add product
            obj.add_items()

        elif op==2: #show categories
            obj.show_categories()
            show_choice=input("Enter the category to view items :")
            obj.show_category_items(show_choice)


        elif op==3: #remove category
            obj.show_categories()
            remove_choice = input("Enter the category to be deleted :")
            obj.remove_category(remove_choice)

        elif op==4: #remove item from category
            obj.show_categories()
            remove_cat_choice=input("Enter the category in which item should be deleted :")
            obj.show_category_items(remove_cat_choice)
            remove_item_choice=input("Enter the item should be deleted :")
            obj.remove_item(remove_item_choice,remove_cat_choice)

        elif op==5: #add to cart
            obj.show_categories()
            add_cart_cat = input("Enter category of item to add to cart :")
            obj.show_category_items(add_cart_cat)
            add_cart_item = input("Enter the item name:")
            obj.add_cart(add_cart_item,add_cart_cat)

        elif op==6:  #remove from cart
            obj.view_cart()
            print("Select the item you need to remove from cart")
            remove_cart_item=input("Enter item :")
            obj.remove_from_cart(remove_cart_item)


        elif op==7:  #view cart
            obj.view_cart()


        elif op==8:  #buy and checkout
            obj.buy_and_checkout()
   

        elif op==9: #exit
            print("Bye")
            break

        else:
            print("Invalid option !")



show_items()
options()
 