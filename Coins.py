def exact_change():

    x = input("Please Enter Change Amount \n")
    
    #converting str -> float -> int to get expected output. 
    #I am doing this check because some users may input their change 
    #in the traditional format but my code expects a single large int

    if "." in x:
        x = float(x)
        x = int(x * 100)
    else:
        x = int(x)

    if x == 0:
        print("no change")
        return 
    
    #dollar check

    num_dollars = x // 100
    remainder = x % 100
    if num_dollars == 1:
        print(num_dollars, "dollar")
    elif num_dollars > 1:
        print(num_dollars, "dollars")
    
    #quarter check

    if remainder > 24: 
        num_quarters = remainder // 25
        remainder = remainder % 25
        if num_quarters == 1:
            print(num_quarters, "quarter")
        elif num_quarters > 1:
            print(num_quarters, "quarters")
    
    #dime check

    if remainder > 9: 
        num_dimes = remainder // 10
        remainder = remainder % 10
        if num_dimes == 1:
            print(num_dimes, "dime")
        elif num_dimes > 1:
            print(num_dimes, "dimes")

    #nickle check

    if remainder > 4:
        num_nickles = remainder // 5
        remainder = remainder % 5
        if num_nickles == 1:
            print(num_nickles, "nickle")
        elif num_nickles > 1:
            print(num_nickles, "nickles")

    #penny check

    if remainder > 0:
        num_pennies = remainder // 1
        if num_pennies == 1:
            print(num_pennies, "penny")
        elif num_pennies > 1:
            print(num_pennies, "pennies")
    
#Final Check

if __name__=="__main__":

    exact_change()
