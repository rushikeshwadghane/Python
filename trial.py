import pandas as pd

# Header
headers = ["Account Name (Debit)", "Debit Amount (₹)", "Account Name (Credit)", "Credit Amount (₹)"]

# Part 1 data
part1_data = [
    ["Opening Balance", 302.44, "Closing Balance", 3.00],
    ["Mr. Ajay", 1548208.00, "Audit Fee Payable", 205000.00],
    ["Dhamani Vikas Yene", 1434208.00, "NPA Payable", 1464832.00],
    ["Bank A/C No. 37 SGM", 2564830.00, "Salary Payable", 242000.00],
    ["1802 M.U.C. Equalized Loan", 1328280.00, "Dhamani Vikas Yene", 403800.00],
    ["1801 Bank M.U. Equalized Loan", 2668155.00, "Bank A/C No. 37 SGM", 1414445.00],
    ["1855 Bank M.U. Installment Loan", 410940.00, "SGM Bank Fixed Deposit", 1416000.00],
    ["1806 Bank M.U. Saraswat Equalized Loan", 1368656.00, "Bank Loan Interest", 2000.00],
    ["Bank M.U. Equalized Loan", 1386280.00, "Bank Swap Fund", 300000.00],
    ["Mr. M.U. Equalized Loan", 1019619.70, "1801 Bank M.U. Equalized Loan", 870070.00]
]

# Part 2 data
part2_data = [
    ["Mr. M.U. Installment Loan", 434506.00, "1855 Bank M.U. Installment Loan", 443940.00],
    ["Mr. M.U. Sasyavatin Equalized Loan", 1160370.00, "1806 Bank M.U. Sasyavatin Equalized Loan", 1368656.00],
    ["Mr. D.C.C. Special Emergency Loan", 256950.00, "Bank M.U. Equalized Loan", 266800.00],
    ["Member Contribution", 124.00, "1801 Bank M.U. Equalized Loan", 205000.00],
    ["Secretary Contribution", 116.00, "Mr. M.U. Installment Loan", 103040.00],
    ["Interest Due Amount", 308848.00, "Mr. M.U. Sasyavatin Equalized Loan", 200000.00],
    ["Interest Free Late Fee Interest", 323920.00, "2002 Bank D.M.U. Emergency Loan", 206040.00],
    ["Interest Due Amount", 228432.00, "Secretary Contribution", 116.00],
    ["Member Interest", 357658.00, "Interest Due Amount", 202800.00],
    ["Penalty Interest", 2050.00, "Interest Free Late Fee Interest", 303920.00],
    ["Admission Fee", 4800.00, "Yene Employee Salary A/c", 4500.00],
    ["NPA Income", 1484215.00, "Interest Due Amount", 192000.00],
    ["Capital Profit", 404247.00, "Furniture & Fixtures", 5000.00],
    ["", "", "Member Interest", 350000.00],
    ["", "", "Stationery", 200000.00],
    ["", "", "Travel", 200000.00],
    ["", "", "Xerox", 15544.00],
    ["", "", "Miscellaneous Expense", 3250.00],
    ["", "", "Bank Interest", 3000.00],
    ["", "", "Salary Payable", 100000.00],
    ["", "", "Pigmy & Other Collection Expense", 120000.00],
    ["", "", "Employee Salary", 250000.00],
    ["", "", "Employee Bonus", 20000.00]
]

# Combine all data
all_data = part1_data + part2_data

# Create DataFrame
df = pd.DataFrame(all_data, columns=headers)

# Save to Excel
df.to_excel("Trial_Balance_Report.xlsx", index=False)
print("Excel file 'Trial_Balance_Report.xlsx' created successfully.")
