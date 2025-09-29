# Exercise 3 - Vanessa Belous

import functools
# use dictionary to store expenses and their amounts in a way to easily pair the data
expenses_dict = {}
# a list stores only the amounts so the reduce method can be used
amount_list = []

# stores input about expenses into a dictionary and separate amount list
def user_input():
    global expenses_dict
    global amount_list

    print("\nPlease enter your expenses this month below, using the format Expense: $00.00")
    print('When finished, submit "Done" to start analysis.\n')

    while True:
        temp_input = input("- ")

        # loop continues writing to dictionary until user is done
        if temp_input == "Done":
            break
        else:
            # store values in dictionary and amounts list
            temp_expense, temp_amount = temp_input.split(": $")
            # add type of expense and expense itself as pairs to a dictionary
            temp_amount = float(temp_amount)
            expenses_dict[temp_amount] = temp_expense
            # add expense itself to a list to compare values
            amount_list.append(float(temp_amount))

def main():
    # call to function that handles input and assigning values to storage
    user_input()

    # lambda function to find most expensive expense
    highest_amount = float(functools.reduce(lambda x, y: x if (x > y) else y, amount_list))
    highest_expense = expenses_dict[highest_amount]

    # lambda function to find cheapest expense
    lowest_amount = float(functools.reduce(lambda x, y: x if (x < y) else y, amount_list))
    lowest_expense = expenses_dict[lowest_amount]

    # lambda function to calculate total expenses
    total_expenses = functools.reduce(lambda x, y: x + y, amount_list)

    # display results
    print("\nThe highest expense is", highest_expense, "at:", f"${highest_amount:,.2f}")
    print("\nThe lowest expense is", lowest_expense, "at:", f"${lowest_amount:,.2f}")
    print("\nYour total monthly expenses come out to:", f"${total_expenses:,.2f}")

main()