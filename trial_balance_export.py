"""Creates an Excel trial-balance example using synthetic account data."""

import pandas as pd


HEADERS = [
    "Debit account",
    "Debit amount",
    "Credit account",
    "Credit amount",
]

ROWS = [
    ["Cash", 1200.00, "Sales revenue", 1200.00],
    ["Office supplies", 85.50, "Accounts payable", 85.50],
    ["Travel expense", 240.00, "Cash", 240.00],
]


def main():
    """Write the synthetic example rows to an Excel spreadsheet."""
    dataframe = pd.DataFrame(ROWS, columns=HEADERS)
    output_path = "trial_balance_report.xlsx"
    dataframe.to_excel(output_path, index=False)
    print(f"Excel file '{output_path}' created successfully.")


if __name__ == "__main__":
    main()
