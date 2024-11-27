#შექმენით ფუნქცია, vending-machine, გექნებათ პროდუქტების სია, მომხმარებელმა, კი უნდა აირჩიოს სასურველი პროდუქტი, თქვენ კი ის უნდა დაუპრინტოთ,

def vending_machine(products):
    print("Available products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product}")

    try:
        choice = int(input("Enter the number of the product you want: "))
        if 1 <= choice <= len(products):
            print(f"You selected: {products[choice - 1]}")
        else:
            print("Invalid selection. Please choose a valid product number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#მაგალითი
products = ["Soda", "Chips", "Candy", "Water", "Juice"]
vending_machine(products)