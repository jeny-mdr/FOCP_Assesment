# Header for the Pizza Price Calculator
header="BPP Pizza Price Calculator"
print(header)

# Header Design for the Pizza Price Calculator
header_design=("=")
print(len(header)*header_design)


# Infinite loop until a valid input is received for the number of pizzas ordered
while True:
        try:
            pizzas_ordered=int(input("\nHow many pizzas ordered? "))
            if pizzas_ordered>0:
                break
            print("Please enter a positive integer!",end="")
        except ValueError:
            print("Please enter a number!",end="")


# Function to get the number of pizzas ordered
def determine_pizzas_ordered():
    """
    Get the number of pizzas ordered.

    Returns:
        int: The number of pizzas ordered.
    """
    return pizzas_ordered


# Infinite loop until valid input for delivery requirement is received
while True:
        try:
            expected_input=["y","n","yes","no"]
            delivery_requirement=input(("Is delivery required? ")).lower()
            if delivery_requirement in expected_input:
                pizzas_ordered=determine_pizzas_ordered()
                delivery_cost = 0 if delivery_requirement in ["no", "n"] else (0 if pizzas_ordered >= 5 else 2.50)
                break
            else:
               print('Please answer "Y" or "N".')

        except ValueError:
            print('Please answer "Y" or "N".')


# Function to get the delivery cost
def determine_delivery_requirement():
    """
    Determine the delivery cost based on the number of pizzas ordered.

    Returns:
        float: The delivery cost, where 0 indicates no delivery cost.
    """
    return delivery_cost


# Infinite loop until valid input for the day of delivery is received
while True:
    try:
        expected_input=["y","n","yes","no"]
        day_of_delivery=input("Is it Tuesday? ").lower()
        if day_of_delivery in expected_input:
            tuesday_discount=0.5 if day_of_delivery=="yes" or day_of_delivery=="y" else 0
            break
        else:
            print('Please answer "Y" or "N".',end="")
    except ValueError:
        print('Please answer "Y" or "N".',end="")


# Function to get tuesday discount
def determine_tuesday_discount():
    """
    Determine the Tuesday discount based on user input.

    Returns:
        float: The Tuesday discount, where 0.5 indicates a discount on Tuesday and 0 indicates no discount.
    """
    return tuesday_discount


# Infinite loop until valid input for app usage is received
while True:
        try:
            expected_input=["y","n","yes","no"]
            use_of_app=input("Did the customer use the app? ").lower()
            if use_of_app in expected_input:
                app_discount=0.25 if use_of_app=="yes" or use_of_app=="y" else 0
                break
            else:
               print('Please answer "Y" or "N".',end="")
        except ValueError:
            print('Please answer "Y" or "N".',end="")


#Function to get app discount           
def determine_app_discount():
    """
    Determine the app discount based on user input.

    Returns:
        float: The app discount, where 0.25 indicates a discount for app usage and 0 indicates no discount.
    """
    return app_discount


#Function to determine total price
def determine_total_price():
    """
    Determine the total price of pizzas, considering various discounts and delivery costs.

    Returns:
        float: The total price of pizzas after applying discounts and delivery costs.
    """
    cost_of_pizza=12
    pizzas_ordered=determine_pizzas_ordered()
    tuesday_discount=determine_tuesday_discount()
    delivery_cost=determine_delivery_requirement()
    price_of_pizza=(cost_of_pizza*pizzas_ordered)-(tuesday_discount*(cost_of_pizza*pizzas_ordered))
    total_price_of_pizza=(price_of_pizza+delivery_cost)-(app_discount*(price_of_pizza+delivery_cost))
    return total_price_of_pizza
    

#Function to call the determine_total_price function to calculate the total price
def main():
    """
    Main function calculates and prints the total price of pizzas.
    
    Returns:
        None
    """
    print(f"\nTotal Price: £{determine_total_price():.2f}.")


#Execute the main function if the script is being run as the main program
if __name__=="__main__":
    main()




   






