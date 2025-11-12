# Ask the user for their monthly income
monthly_income=int(input("enter your monthly income: "))
# Ask the user for their monthly expenses
monthly_expenses=int(input("enter your total monthly expenses: "))
#Calculation of Monthly Savings:
monthly_savings= monthly_income - monthly_expenses
#projecting Annual Savings after one year, incorporating the interest
# Assume an annual interest rate of 5%
interest_rate=0.05
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)
# Display results
print("\n--- Savings Summary ---")
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected savings after one year (with 5% interest) are: ${projected_savings:.2f}")
