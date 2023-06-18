
def generateMenu(products,prices):
    for i in range(len(products)):
        print(f"{i+1}) {products[i]} - ${prices[i]}")
    print("5) Total to pay")


def addCoffe(prices,option,total):
    for i in range(len(prices)):
        if (i+1) == option:
             total += prices[i]
    return total
            