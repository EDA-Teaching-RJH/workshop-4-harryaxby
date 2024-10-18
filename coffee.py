
coffee_price = 75
hotc = 100
print("this coffee machine only accepts 50p, 20p, 10p and 5p, coffee is 75p")
while True:   
    if coffee_price <= 0:
        break     
    
    money = int(input("please insert money "))
    
    def done():
            x = coffee_price * -1
            print("you have entered enough money, you are owed ",x, "p change.")
       
    if money == 50:
        coffee_price = coffee_price - 50
        if coffee_price <0:
            done()
        else:
            print("remaing price to pay is",coffee_price,"p")
    
    elif money == 20:
        coffee_price = coffee_price - 20
        if coffee_price <0:
            done()
        else:
            print("remaing price to pay is",coffee_price,"p")

    elif money == 10:
        coffee_price = coffee_price - 10
        if coffee_price <0:
            done()
        else:
            print("remaing price to pay is",coffee_price,"p")

    elif money == 5:
        coffee_price = coffee_price - 5
        if coffee_price <0:
            done()
        else:
            print("remaing price to pay is",coffee_price,"p")
    
    else:
        print("invalid currency")


    