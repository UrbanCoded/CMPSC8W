def exact_change(user_input):

    if "." in user_input:
        user_input = float(user_input * 100)
        user_input = int(user_input)

    if user_input <= 0:
        print("no change")

    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

    num_dollars = user_input // 100
    if num_dollars > 0 and user_input > 0:
        user_input = user_input - (num_dollars * 100)
    if num_dollars == 1:
        print(num_dollars, "dollar")
    elif num_dollars > 1:
        print(num_dollars, "dollars")
    
    num_quarters = user_input // 25
    if num_quarters > 0 and user_input > 0:
        user_input = user_input - (num_quarters * 25)
    if num_quarters == 1:
        print(num_quarters, "quarter")
    elif num_quarters > 1:
        print(num_quarters, "quarters")
    
    num_dimes = user_input // 10
    if num_dimes > 0 and user_input > 0:
        user_input = user_input - (num_dimes * 10)
    if num_dimes == 1:
        print(num_dimes, "dime")
    elif num_dimes > 1:
        print(num_dimes, "dimes")
    
    num_nickels = user_input // 5
    if num_nickels > 0 and user_input > 0:
        user_input = user_input - (num_nickels * 5)
    if num_nickels == 1:
        print(num_nickels, "nickel")
    elif num_nickels > 1:
        print(num_nickels, "nickels")

    num_pennies = user_input // 1
    if num_pennies > 0 and user_input > 0:
        user_input = user_input - (num_pennies * 1)
    if num_pennies == 1:
        print(num_pennies, "penny")
    elif num_pennies > 1:
        print(num_pennies, "pennies")

    return(num_dollars, num_quarters, num_dimes, num_nickels, num_pennies)

if __name__ == "__main__":

    user_total = input("Please Input Value \n")
    exact_change(user_total)
