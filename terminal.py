class Item:
    def __init__(self, init_name, init_price, init_inventory = 0):
        self.name = init_name
        self.price = init_price
        self.inventory = init_inventory

    def __str__(self):
        return self.name

class Customer:
    def __init__(self, init_customer_number, init_name, init_birthday = None):
        self.name = init_name
        self.customer_number = init_customer_number
        self.birthday = init_birthday

    def get_customer():
        cust_num = int(input('Please enter customer number: '))
        if cust_num <= len(members) and cust_num > 0:
            customer = members[cust_num - 1]
        else:
            print('Error: Invalid Customer Number')
            customer = None
        return customer

    def __str__(self):
        return self.name

class Terminal:
    def __init__(self, init_store_name = 'Unknown Store'):
        self.store_name = init_store_name

    def welcome(self):
        print('Hello! Welcome to ' + self.store_name + '.')
        customer = Customer.get_customer()
        print('Hello, ' + customer.name + '.')
        return customer

def add_items():
    for i in range(len(items)):
        if items[i].inventory > 0:
            print(i+1, items[i].name, items[i].price)
    chosen_item = items[int(input('Please enter item number: ')) - 1]
    item_quantity = int(input('How many do you want? '))
    order[chosen_item] = item_quantity
    print('Okay, I added ' + str(item_quantity) + ' of ' + chosen_item.name + ' to your order.')
    print(order)
    another_item = input('Add another item? ')
    if another_item == 'y' or another_item == 'yes':
        print(chosen_item.inventory)
        chosen_item.inventory += (-(item_quantity))
        print(chosen_item.inventory)
        add_items()
    return order


members = [
  Customer(1, 'Harry', 'July 31, 1980'),
  Customer(2, 'Ken', 'July 3, 1988')
]

items = [
  Item('Python Textbook', 13.99, 20),
  Item('MacBook', 1199.99, 15),
  Item('Extended Warranty', 49.99, 12)
]

order = {}

def main():
    terminal = Terminal('Brosso\'s')
    customer = terminal.welcome()
    cust_order = add_items()

if __name__ == "__main__":
    main()
