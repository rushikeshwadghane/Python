"""Compares table names in a SQL delete script with an expected table list."""

import re


EXPECTED_TABLES = {
    "orders",
    "orders_history",
    "order_items",
    "payments",
}

DELETE_SCRIPT = """
DELETE FROM orders;
DELETE FROM orders_history;
DELETE FROM order_items;
"""


def find_missing_tables(expected_tables, sql_script):
    """Return expected table names that do not appear in DELETE statements."""
    used_tables = {
        table.lower()
        for table in re.findall(
            r"\bDELETE\s+FROM\s+([A-Za-z_]\w*)",
            sql_script,
            flags=re.IGNORECASE,
        )
    }
    return set(expected_tables) - used_tables


if __name__ == "__main__":
    missing_tables = find_missing_tables(EXPECTED_TABLES, DELETE_SCRIPT)
    print("Tables missing from the DELETE script:")
    for table in sorted(missing_tables):
        print(table)
