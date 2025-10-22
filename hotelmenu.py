#define the resturant 
menu = {
    'Pasta': 12.99,
    'Burger': 9.99,
    'Salad': 7.99,
    'Pizza': 11.99,
    'Coffee': 3.99
}
#Great
print("welcome to our python restaurant!")
print("pasta - $12.99")
print("burger - $9.99")
print("salad - $7.99")
print("pizza - $11.99")
print("coffee - $3.99") 

order_total = 0 
#12.99 + 9.99 + 3.99 = 26.97 

item_1 = input("enter the name of item you want to order=")
if item_1 in menu:
     order_total += menu[item_1] #0 + 50
     print(f"Your item {item_1} has been added to your order")
else:
        print(f"Ordered item {item_1} is not available")

        another_order = input("do you want to add another item? (yes/no)=")
        item_2 = input("enter the name of second item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your item {item_2} has been added to your order")
        else:
            print(f"Ordered item {item_2} is not available")

print(f"The total order amount of items to pay is  ${order_total}")
