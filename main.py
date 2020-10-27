# Matthew James Resendez
# 1431242
class ItemToPurchase:
    def __init__(self):
        self.iname = "none"
        self.iprice = 0
        self.iquantity = 0

    def print_icost(self):
        print(self.iname + " " + str(self.iquantity) + " @ $" + str(self.iprice) + " = $" +
              str(self.iprice * self.iquantity))
if __name__ == '__main__':
    print("Item 1")
    item1 = ItemToPurchase()
    item1.iname = input('Enter the item name:\n')
    item1.iprice = int(input('Enter the item price:\n'))
    item1.iquantity = int(input('Enter the item quantity:\n'))

    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.iname = input('Enter the item name:\n')
    item2.iprice = int(input('Enter the item price:\n'))
    item2.iquantity = int(input('Enter the item quantity:\n'))

    print("\nTOTAL COST")
    item1.print_icost()
    item2.print_icost()

    total = (item1.iprice * item1.iquantity) + (item2.iprice * item2.iquantity)

    print("\nTotal: $" + str(total))