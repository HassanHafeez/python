def calculate_tax(income):
    if income <= 10000:
        tax_rate = 0
    elif income <= 30000:
        tax_rate = 0.1
    elif income <= 60000:
        tax_rate = 0.2
    else:
        tax_rate = 0.3

    tax = income * tax_rate
    return tax


# Input income
income = float(input("Enter your income: "))

# Calculate tax
tax = calculate_tax(income)

# Output tax
print(f"Your tax is: ${tax:.2f}")
