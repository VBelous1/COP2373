# Exercise 1 - Vanessa Belous

# Global Variables
remaining_tickets = 10
total_customers = 0

# subtracts tickets bought from remaining tickets; tallies total customers
def buy_tickets(order):
    global remaining_tickets
    global total_customers

    if order <= remaining_tickets:
        remaining_tickets -= order
        total_customers += 1
        return True
    else:
        return False

# allows customers to place their order
def customer_prompt():
    global remaining_tickets
    order = 0
    can_buy = True

    while remaining_tickets > 0:
        order = int(input("\nHow many tickets would you like to purchase today? "))
        if order <= 4:
            can_buy = buy_tickets(order)
            if can_buy == False:
                print("\nOops! There are only ", remaining_tickets, " tickets remaining.")
            else:
                print("Tickets Available: ", remaining_tickets)
        else:
            print("Presale tickets are limited to four per customer!")


print("Welcome to Vanessa's Cinema!")
print("(Presale tickets are limited to four per customer.)")
print("Available Tickets: 10")

customer_prompt()
print("\nAll tickets available for pre-sale have been sold!")
print("Total customers:", total_customers)
