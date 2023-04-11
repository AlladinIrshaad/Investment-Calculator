# ************************************************* Capstone Project *************************************************
# We have to create a program that allows users to access 2 different financial calculators, investment and home loan repayment calculator
# Importing the Math module
import math

# User needs to see below output and choose betwwen investment or bond calculator
print("Welcome to the InterGalactic Bank investment calculator, assist you we can the following with: ")
print()
print("Investment - to calculate the amount of interest you will earn on your investment")
print("Bond - to calculate the amount you will have to pay on your bond")

print()

while True:
    try:
        choices=input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ")
        if choices.lower() not in ["investment", "bond"]:   
            # Raise a ValueError if the user input is not investment or bond.
            raise ValueError("Invalid choice")
        break
    except ValueError as error:
        print(error)

# Investment selection
# Asking user the amount of money they wish to deposit, interest rate and number of years.
if choices.lower() == "investment":
    while True:
        try:
            p_amount = input("How much money are you depositing: ")
            if not p_amount.isdigit():    # Ref: https://www.w3schools.com/python/ref_string_isdigit.asp 
                raise ValueError("Invalid entry. Please enter a correct amount.")   # exception error handling
            p_amount = float(p_amount)
            break
        except ValueError as error:
            print(error)
    
    while True:
        try:
            r_rate = input("Please enter the interest rate (Number only): ")
            if not r_rate.replace('.', '').isdigit():    
                raise ValueError("Invalid entry. Please enter a number only for the interest rate.")
            r_rate = float(r_rate) / 100    # convert the interest rate to a decimal
            break
        except ValueError as error:
            print(error)

    while True:
        try:
            t_years = input("Number of years you wish to invest for: ")
            if not t_years.isdigit():
                raise ValueError("Invalid entry. Please enter correct number of years.")
            t_years = int(t_years)
            break
        except ValueError as error:
            print(error)

# Asking user if they want simple or compund interest
    while True:
        try:
            interest = input("Please choose between 'Simple' or 'Compound' interest: ")
            if interest.lower() not in ["simple", "compound"]:
                raise ValueError("Invalid entry.")
            break
        except ValueError as error:
            print(error)
    
    # Calculations and output       
    if interest.lower() == 'simple':
        total_amount = p_amount * (1 + (r_rate * t_years))  
        print(f"The Total amount of interest you will earn on your investment is: R{total_amount:.2f} over {t_years} years")
        
    elif interest.lower() == 'compound':
        total_amount = p_amount * math.pow((1+r_rate),t_years)
        print(f"The Total amount of interest you will earn on your investment is: R{total_amount:.2f} over {t_years} years")
        
# Bond calculator
# Asking user value of the property, interest rate and term of the loan
if choices.lower() == "bond":
    while True:
        try:
            p_value = input("What is the estimate value of the property: ")
            if not p_value.isdigit():   
                raise ValueError("Invalid entry. Please enter a correct amount.")
            p_value = float(p_value)
            break
        except ValueError as error:
            print(error)
    
    while True:
        try:
            i_rate_input = input("Please enter the interest rate (Number only): ")
            if not i_rate_input.replace('.', '').isdigit():
                raise ValueError("Invalid entry. Please enter a number only for the interest rate.")
            i_rate = float(i_rate_input) / 100 / 12  # convert the interest rate to a decimal
            break
        except ValueError as error:
            print(error)

            
    while True:
        try:
            n_months = input("Term of the loan (Months): ")
            if not n_months.isdigit():
                raise ValueError("Invalid entry. Please enter the correct number of months.")
            n_months = int(n_months)
            try:
                if n_months < 120 or n_months > 360: 
                    raise ValueError("Invalid entry. Number of months can not be less than 120 or more than 360 months.")
                break
            except ValueError as error:
                print(error)
        except ValueError as error:
            print(error)
    
    # Calculations and output        
    repayment = (i_rate * p_value) / (1-(1+i_rate)**(-n_months))
    print(f"Your monthly installment will be: R{repayment:.2f} over {n_months} months with an interest rate of {i_rate_input}%")
    


