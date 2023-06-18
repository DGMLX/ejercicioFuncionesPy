'En una cafetería se venden 4 tipos de cafés:• Espresso $1.500• Capuchino $1.800• Latte $1.600• Moca $1.700Determine el total a pagar por un cliente que puede llevar varios cafés y aplique eldescuento del 10% al total a pagar, si su compra es superior o igual a $3.000.Considere crear un menú de opciones y calcule el monto utilizando función'
import funciones4 as fn

products = ["Espresso","Capuchino","Latte","Moca"]
prices = [1500,1800,1600,1700]
total = 0 

while True:
    fn.generateMenu(products,prices)
    try:
        option = int(input("Choose a coffe: "))
        if option > 0 and option <5:
            total = fn.addCoffe(prices,option,total)
        elif option == 5:
            if total >= 3000:
                print(f"Total to pay with 10% dsct : ${total-(total*0.1)}")
                break
            else:
                print(f"Total to pay : ${total}")
                break        
        else:
            print("You have to choose a valid option.")
    except:
        print("You have to write a numeric value.")