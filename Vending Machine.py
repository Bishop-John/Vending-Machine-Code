print ("Welcome to the Python Vending Machine.")

#Asking the user how much money they wish to enter.
pounds = int(input("How many pounds do you wish to insert?"))
pence = float(input("How many pence do you wish to insert?"))
# Creating a variable to store the total amount of money inserted into the vending machine.
change = round(pounds + pence,2)
purchases = []

# Informing the user how much they have entered in total.
print ("\nIn total you have entered £", change)

# Creating variables for the 5 products and their respective prices. 
product_1, product_1_price = "Flake", 0.55
product_2, product_2_price = "Wispa", 0.50
product_3, product_3_price = "Crunchie", 0.65
product_4, product_4_price = "Milky Way", 0.35
product_5, product_5_price = "Boost", 0.65

# Creating variables to track the number of each items bought.
flakes_bought, wispas_bought, crunchies_bought, milky_ways_bought, boosts_bought = 0, 0, 0, 0, 0

# Informing the user of the choices available and the prices that of each item.
print ("There are 5 products available to pick from;\n")

print ("Item: {}, Price {} ".format(product_1, product_1_price))
print ("Item: {}, Price {} ".format(product_2, product_2_price))
print ("Item: {}, Price {} ".format(product_3, product_3_price))
print ("Item: {}, Price {} ".format(product_4, product_4_price))
print ("Item: {}, Price {} ".format(product_5, product_5_price))
print ("")

# Asking the user to make a selection.
while change > 0:
    customer_choice = input("What would you like to buy? Type N when you are finished \n").upper()
    if customer_choice == "FLAKE" and change >= product_1_price:
        print ("You have chosen a", product_1, "these cost", product_1_price, "each,")
        change = round((change - product_1_price),2)
        purchases.append("Flake")
        print ("You have this much money remaining: £", change)
    elif customer_choice == "WISPA" and change >= product_2_price:
        print ("You have chosen a", product_2, "these cost", product_2_price, "each,")
        change = round((change - product_2_price),2)
        purchases.append("Wispa")
        print ("You have this much money remaining: £", change)
    elif customer_choice == "CRUNCHIE" and change >= product_3_price:
        print ("You have chosen a", product_3, "these cost", product_3_price, "each,")
        change = round((change - product_3_price),2)
        purchases.append("Crunchie")
        print ("You have this much money remaining: £", change)
    elif customer_choice == "MILKY WAY" and change >= product_4_price:
        print ("You have chosen a", product_4, "these cost", product_4_price, "each,")
        change = round((change - product_4_price),2)
        purchases.append("Milky Way")
        print ("You have this much money remaining: £", change)
    elif customer_choice == "BOOST" and change >= product_5_price:
        print ("You have chosen a", product_5, "these cost", product_5_price, "each,")
        change = round((change - product_5_price),2)
        purchases.append("Boost")
        print ("You have this much money remaining: £", change)
    elif customer_choice == "N" or customer_choice == "n":
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ", purchases)
        print ("You have £", change, "remaining.")
        break
    else:
        print ("There has been an error or you may not have enough credit.")        

