# Ask the user for their monthly income
monthly_income=int(input("enter your monthly income: "))
# Ask the user for their monthly expenses
monthly_expenses=int(input("enter your total monthly expenses: "))
#Calculation of Monthly Savings:
monthly_savings= monthly_income - monthly_expenses
#projecting Annual Savings after one year, incorporating the interest
interest_rate=5%     #This is simple annual interest rate
projected_savings= monthly_savings * 12 + (monthly_savings * 12 * 0.05))
# Display results
print("\n--- Savings Summary ---")
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected savings after one year (with 5% interest) are: ${projected_savings:.2f}")
