import math
#user prompted to choose a bond or investment calculator
print("Investment - to calculate the amount of interest you'll earn in interest ")
print("Bond       - to calculate the amount you'll have to pay on a home loan \n")
print("Choose either 'investment' or 'bond' from the menu above to proceed: \n")
#user inputs selection
choice = input("Enter your choice: ").lower()
#output if investment is selected 
if choice == "investment":
        P = float(input("Input the amount you are depositing: "))
        r = float(input("Input the interest rate: "))/100
        t = float(input("Input the number of years to invest for: "))
        interest = input("Do you want simple or compound interest: ").lower()
        if interest == "simple":
            A_simple = (P*(1+r*t))
            print(f"Your total simple interest is £{A_simple:.2f}")
        elif interest == "compound":
            A_compound = (P*math.pow((1+r),t))
            print(f"Your total compound interest is £{A_compound:.2f}")
#output if bond is selected    
elif choice == "bond":
        P = float(input("Input the present(current) value of your house: "))
        i = float(input("Input the interest rate: "))/100
        n = float(input("Input the number of months for the bond: "))
        repayment = ((i/12)*P)/(1-math.pow((1+(i/12)),((-n))))
        print(f"Your monthly repayment is £{repayment:.2f}")
#output if selection is not investment or bond
else:
     choice != "investment" or choice != "bond"
     print("Please only select Investment or Bond.")  