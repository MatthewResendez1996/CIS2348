##Matthew James Resendez
##1431242

def exact_change(user_total):
    if (user_total <= 0):
        return None, None, None, None, None
    else:
        dollars = user_total // 100
        user_total %= 100

        quarters = user_total // 25
        user_total %= 25

        dimes = user_total // 10
        user_total %= 10

        nickels = user_total // 5
        pennies = user_total % 5

        return (dollars, quarters, dimes, nickels, pennies)


if __name__ == '__main__':
    useramount = int(input())
    dollars, quarters, dimes, nickels, pennies = exact_change(useramount)
    if (dollars == None):
        print("no change")
    else:
        if dollars > 0:
            if dollars == 1:
                print('%d dollar' % dollars)
            else:
                print('%d dollars' % dollars)

    if quarters > 0:
        if quarters == 1:
            print('%d quarter' % quarters)
        else:
            print('%d quarters' % quarters)

    if dimes > 0:
        if dimes == 1:
            print('%d dime' % dimes)
        else:
            print('%d dimes' % dimes)

    if nickels > 0:
        if nickels == 1:
            print('%d nickel' % nickels)
        else:
            print('%d nickels' % nickels)

    if pennies > 0:
        if pennies == 1:
            print('%d penny' % pennies)
        else:
            print('%d pennies' % pennies)